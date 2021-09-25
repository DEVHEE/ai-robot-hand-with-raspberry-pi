"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

# Import modules.
import os
import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound

# Set assets infos.
imgAssets = "./assets/image/"
imgName = "test.png"
imgPath = imgAssets + imgName

tempAssets = "./assets/temp/"
tempName = "temp.png"
tempPath = tempAssets + tempName

# Set results infos.
ttsResults = "./result/tts/"
ttsString = "string.txt"
ttsAudio = "tts.mp3"
ttsStringPath = ttsResults + ttsString
ttsAudioPath = ttsResults + ttsAudio

# Set the test image.
img = cv2.imread(imgPath)
# Obtain only the string from images without visual feedback.
# print(pytesseract.image_to_string(img))

# Obtain the height and width for each image.
hImg, wImg, none = img.shape
# print(img.shape)

# Convert images into bounding box values: x, y, width and height
box = pytesseract.image_to_boxes(img)
# print(box)

# Convert images into bound data values:
# level, page no, block no, paragraph no, line no, word no, x, y, width, height, conf, value
data = pytesseract.image_to_data(img)
# print(data)


# Function for character recognition.
def char():
    for a in box.splitlines():
        # Converts 'box' string into a list stored in 'a'.
        a = a.split()
        # Storing values in the right variables.
        x, y = int(a[1]), int(a[2])
        w, h = int(a[3]), int(a[4])
        # Display bounding box of each letter.
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (255, 0, 0), 1)
        # Display detected letter under each bounding box.
        cv2.putText(img, a[0], (x, hImg - y - 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 1)
    # Output the bounding box with the image.
    cv2.imshow("Recognition Result - Char", img)
    cv2.waitKey(0)


# Function for word recognition.
def word():
    for z, a in enumerate(data.splitlines()):
        # Counter
        if z != 0:
            # Converts 'data' string into a list stored in 'a'.
            a = a.split()
            # Checking if array contains a word.
            if len(a) == 12:
                # Storing values in the right variables.
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                # Display bounding box of each word.
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
                # Display detected word under each bounding box.
                cv2.putText(img, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
    # Output the bounding box with the image.
    cv2.imshow("Recognition Result - Word", img)
    cv2.waitKey(0)


# Function for image capture recognition.
def image():
    # Video feed start.
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow("camera", frame)
                if cv2.waitKey(1) != -1:
                    cv2.imwrite(tempPath, frame)
                    break
            else:
                print("no frame")
                break
    else:
        print("no camera")
        cap.release()
        cv2.destroyAllWindows()
    
    # Assign file and data.
    capImg_file = cv2.imread(tempPath)
    capImg_data = pytesseract.image_to_data(capImg_file)
        
    for z, a in enumerate(capImg_data.splitlines()):
        # Counter
        if z != 0:
            # Converts 'data' string into a list stored in 'a'.
            a = a.split()
            # Checking if array contains a word.
            if len(a) == 12:
                # Storing values in the right variables.
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                # Display bounding box of each word.
                cv2.rectangle(capImg_file, (x, y), (x + w, y + h), (0, 0, 255), 1)
                # Display detected word under each bounding box.
                cv2.putText(capImg_file, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
    # Output the bounding box with the image.
    cv2.imshow("Recognition Output - Image", capImg_file)
    cv2.waitKey(0)
    tempFile = tempPath
    if os.path.isfile(tempFile):
        os.remove(tempFile)


# Function for video capture recognition.
def video():
    # Video feed start.
    cap = cv2.VideoCapture(0)

    # Setting width and height for video feed.
    cap.set(3, 640)
    cap.set(4, 480)

    # Allows continuous frames.
    while True:
        # Capture each frame from the video feed.
        extra, capVid_frames = cap.read()
        capVid_data = pytesseract.image_to_data(capVid_frames)
        for z, a in enumerate(capVid_data.splitlines()):
            # Counter
            if z != 0:
                # Converts 'data' string into a list stored in 'a'.
                a = a.split()
                # Checking if array contains a word.
                if len(a) == 12:
                    # Storing values in the right variables.
                    x, y = int(a[6]), int(a[7])
                    w, h = int(a[8]), int(a[9])
                    # Display bounding box of each word.
                    cv2.rectangle(capVid_frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    # Display detected word under each bounding box.
                    cv2.putText(capVid_frames, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
        # Output the bounding box with the image.
        cv2.imshow("Recognition Output - Video", capVid_frames)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            video.release()
            cv2.destroyAllWindows()
            break


# Function for image(word) recognition with tts.
def tts():
    # Open the file with write permission.
    filewrite = open(ttsStringPath, "w")
    for z, a in enumerate(data.splitlines()):
        # Counter
        if z != 0:
            # Converts 'data' string into a list stored in 'a'.
            a = a.split()
            # Checking if array contains a word.
            if len(a) == 12:
                # Storing values in the right variables.
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                # Display bounding box of each word.
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
                # Display detected word under each bounding box.
                cv2.putText(img, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
                # Writing to the file.
                filewrite.write(a[11] + " ")
    filewrite.close()
    # Open the file with read permission.
    fileread = open(ttsStringPath, "r")
    language = "en"
    line = fileread.read()
    if line != " ":
        fileread.close()
        speech = gTTS(text=line, lang=language, slow=False)
        speech.save(ttsAudioPath)
    # Output the bounding box with the image.
    cv2.imshow("Recognition Result - TTS", img)
    cv2.waitKey(0)
    playsound(ttsAudioPath)


# Select the recognition option.
while True:
    option = input("--------------------\nSelect the recognition option.\n[1] Char\n[2] Word\n[3] Image\n[4] Video\n[5] TTS\n--------------------\nSELECT: ")
    print("\n")
    if option == '1':
        char()
    elif option == '2':
        word()
    elif option == '3':
        image()
    elif option == '4':
        video()
    elif option == '5':
        tts()
    else:
        break
