"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

# Import modules.
from . import pwm_settings as pwm

# Function of control finger 1.
def ctrlFin1(L01, L12):
    if (L01 >= 0 and L12 > 0):
        print("o", end='')
        pwm.device.set_pwm(0, 0, pwm.servo_0)  # Rotate servo 0 degrees.
    elif (L01 < 0 and L12 > 0):
        print("o", end='')
        pwm.device.set_pwm(0, 0, pwm.servo_0)  # Rotate servo 0 degrees.
    else:
        print("I", end='')
        pwm.device.set_pwm(0, 0, pwm.servo_180)  # Rotate servo 180 degrees.

# Function of control finger 2.
def ctrlFin2(L01, L12):
    if (L01 >= 0 and L12 > 0):
        print("o", end='')
    elif (L01 < 0 and L12 > 0):
        print("o", end='')
    else:
        print("I", end='')

# Function of control finger 3.
def ctrlFin3(L01, L12):
    if (L01 >= 0 and L12 > 0):
        print("o", end='')
    elif (L01 < 0 and L12 > 0):
        print("o", end='')
    else:
        print("I", end='')

# Function of control finger 4.
def ctrlFin4(L01, L12):
    if (L01 >= 0 and L12 > 0):
        print("o")
    elif (L01 < 0 and L12 > 0):
        print("o")
    else:
        print("I")