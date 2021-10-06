"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

# Import modules.
import time
from . import pwm_settings as pwm

# Initializing servo motor position.
pwm.device.set_pwm(0, 0, pwm.servo_180)
pwm.device.set_pwm(1, 0, pwm.servo_180)
pwm.device.set_pwm(2, 0, pwm.servo_180)

time.sleep(1)

pwm.device.set_pwm(0, 0, pwm.servo_0)
pwm.device.set_pwm(1, 0, pwm.servo_0)
pwm.device.set_pwm(2, 0, pwm.servo_0)

time.sleep(1)


# Function of speech processing.
def speech(last):
    char_speech = [s for s in last]
    move(char_speech)


# Function of movement for each alphabet.
def move(char):
    for c in char:
        if c == "a":
            print(f"Movement of char '{c}'")
            pwm.device.set_pwm(2, 0, pwm.servo_0)
            time.sleep(1)

        elif c == "b":
            print(f"Movement of char '{c}'")
            pwm.device.set_pwm(2, 0, pwm.servo_180)
            time.sleep(1)

        elif c == "c":
            print(f"Movement of char '{c}'")

        elif c == "d":
            print(f"Movement of char '{c}'")

        elif c == "e":
            print(f"Movement of char '{c}'")

        elif c == "f":
            print(f"Movement of char '{c}'")

        elif c == "g":
            print(f"Movement of char '{c}'")

        elif c == "h":
            print(f"Movement of char '{c}'")

        elif c == "i":
            print(f"Movement of char '{c}'")

        elif c == "j":
            print(f"Movement of char '{c}'")

        elif c == "k":
            print(f"Movement of char '{c}'")

        elif c == "l":
            print(f"Movement of char '{c}'")

        elif c == "m":
            print(f"Movement of char '{c}'")

        elif c == "n":
            print(f"Movement of char '{c}'")
            pwm.device.set_pwm(2, 0, pwm.servo_180)
            time.sleep(1)

        elif c == "o":
            print(f"Movement of char '{c}'")

        elif c == "p":
            print(f"Movement of char '{c}'")

        elif c == "q":
            print(f"Movement of char '{c}'")

        elif c == "r":
            print(f"Movement of char '{c}'")

        elif c == "s":
            print(f"Movement of char '{c}'")

        elif c == "t":
            print(f"Movement of char '{c}'")

        elif c == "u":
            print(f"Movement of char '{c}'")

        elif c == "v":
            print(f"Movement of char '{c}'")

        elif c == "w":
            print(f"Movement of char '{c}'")

        elif c == "x":
            print(f"Movement of char '{c}'")

        elif c == "y":
            print(f"Movement of char '{c}'")

        elif c == "z":
            print(f"Movement of char '{c}'")

        else:
            print(f"Pass unknown char '{c}'")
