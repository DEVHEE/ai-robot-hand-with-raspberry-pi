"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.

watson-streaming-stt
COPYRIGHT © 2016 IBM. ALL RIGHTS RESERVED.
"""

# Import modules.
import argparse
import base64
import configparser
import json
import threading
import time
import os

import pyaudio
import websocket
from websocket._abnf import ABNF

# Setting audio parameters.
CHUNK = 1024
FORMAT = pyaudio.paInt16
# Even if your default input is multi channel (like a webcam mic),
# it's really important to only record 1 channel, as the STT service
# does not do anything useful with stereo. You get a lot of "hmmm" back.
CHANNELS = 1
# Rate is important, nothing works without it. This is a pretty
# standard default. If you have an audio device that requires
# something different, change this.
RATE = 44100
RECORD_SECONDS = 5
FINALS = []
LAST = None

# There is a possibility of API server change, so you need to check Watson's document.
REGION_MAP = {
    'us-south': 'stream.watsonplatform.net',
}


def read_audio(ws, timeout):
    """
    Read audio and sent it to the websocket port.
    This uses pyaudio to read from a device in chunks and send these
    over the websocket wire.
    """
    global RATE
    p = pyaudio.PyAudio()
    RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")
    rec = timeout or RECORD_SECONDS

    for i in range(0, int(RATE / CHUNK * rec)):
        data = stream.read(CHUNK)
        # print("Sending packet... %d" % i)
        ws.send(data, ABNF.OPCODE_BINARY)

    # Disconnect the audio stream
    stream.stop_stream()
    stream.close()
    print("Done recording!")

    # In order to get a final response from STT we send a stop, this
    # will force a final=True return message.
    data = {"action": "stop"}
    ws.send(json.dumps(data).encode('utf8'))
    # ... which we need to wait for before we shutdown the websocket
    time.sleep(1)
    ws.close()

    # ... and kill the audio device
    p.terminate()


def on_message(self, msg):
    """
    Print whatever messages come in.
    While we are processing any non trivial stream of speech Watson
    will start chunking results into bits of transcripts that it
    considers "final", and start on a new stretch. It's not always
    clear why it does this. However, it means that as we are
    processing text, any time we see a final chunk, we need to save it
    off for later.
    """

    global LAST
    data = json.loads(msg)
    if "results" in data:
        if data["results"][0]["final"]:
            FINALS.append(data)
            LAST = None
        else:
            LAST = data
        # This prints out the current fragment that we are working on.
        print(data['results'][0]['alternatives'][0]['transcript'])

        output = open("./text_output.txt", 'a')
        output.write("\n")
        output.write(data['results'][0]['alternatives'][0]['transcript'])


def on_error(self, error):
    """
    Print any errors.
    """
    print(error)


def on_close(ws):
    """
    Upon close, print the complete and final transcript.
    """
    global LAST
    if LAST:
        FINALS.append(LAST)
    transcript = "".join([x['results'][0]['alternatives'][0]['transcript'] for x in FINALS])
    print(transcript)


def on_open(ws):
    """
    Triggered as soon a we have an active connection.
    """
    args = ws.args
    data = {
        "action": "start",
        # this means we get to send it straight raw sampling
        "content-type": "audio/l16;rate=%d" % RATE,
        "continuous": True,
        "interim_results": True,
        # "inactivity_timeout": 5, # in order to use this effectively
        # you need other tests to handle what happens if the socket is
        # closed by the server.
        "word_confidence": True,
        "timestamps": True,
        "max_alternatives": 3
    }

    # Send the initial control message which sets expectations for the
    # binary stream that follows:
    ws.send(json.dumps(data).encode('utf8'))
    # Spin off a dedicated thread where we are going to read and
    # stream out audio.
    threading.Thread(target=read_audio,
                     args=(ws, args.timeout)).start()


def get_url():
    config = configparser.RawConfigParser()
    config.read('speech.cfg')
    # See
    # https://console.bluemix.net/docs/services/speech-to-text/websockets.html#websockets
    # for details on which endpoints are for each region.
    credential = config.get('auth', 'credential')
    with open(credential) as json_crd:
        crd_data = json.load(json_crd)
        region = crd_data["region"]
        print("SERVER REGION:", region)
    host = REGION_MAP[region]
    return ("wss://{}/speech-to-text/api/v1/recognize?model=en-US_BroadbandModel").format(host)


def get_auth():
    config = configparser.RawConfigParser()
    config.read('speech.cfg')
    credential = config.get('auth', 'credential')
    with open(credential) as json_crd:
        crd_data = json.load(json_crd)
        apikey = crd_data["apikey"]
        print("SERVER APIKEY:", apikey[-5:])
    return ("apikey", apikey)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Transcribe Watson text in real time')
    parser.add_argument('-t', '--timeout', type=int, default=5)
    # parser.add_argument('-d', '--device')
    # parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    return args


def main():
    # Connect to websocket interfaces
    headers = {}
    userpass = ":".join(get_auth())
    headers["Authorization"] = "Basic " + base64.b64encode(
        userpass.encode()).decode()
    url = get_url()

    # If you really want to see everything going across the wire,
    # uncomment this. However realize the trace is going to also do
    # things like dump the binary sound packets in text in the console.
    #
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                                header=headers,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.args = parse_args()
    # This gives control over the WebSocketApp. This is a blocking
    # call, so it won't return until the ws.close() gets called (after
    # 6 seconds in the dedicated thread).
    ws.run_forever()


if __name__ == "__main__":
    output_file = "./text_output.txt"
    if os.path.isfile(output_file):
        os.remove(output_file)

    main()

    print("Now speech processing...")

    # Code for test output.
    output = open("./text_output.txt", 'w')
    output.write("hello")
    output.write("\n")
    output.write("banana")
    output.close()

    # Read saved output file.
    with open(output_file, "r") as f:
        lines = f.read().splitlines()
    last_line = lines[-1:][0]  # Get last line.

    print("DETECTED SPEECH:", last_line)
