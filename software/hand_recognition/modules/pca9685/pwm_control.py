"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

# Import modules.
import time
import math
from . import pwm_settings as pwm


# Initializing servo motor position.
pwm.device.set_pwm(0, 0, pwm.servo_0)
pwm.device.set_pwm(1, 0, pwm.servo_0)
pwm.device.set_pwm(2, 0, pwm.servo_0)

time.sleep(1)

pwm.device.set_pwm(0, 0, pwm.servo_90)
pwm.device.set_pwm(1, 0, pwm.servo_90)
pwm.device.set_pwm(2, 0, pwm.servo_90)


# Function of control finger 1.
def ctrlFin1(resList, saveList):
    # Place the result elements in the list.
    res01 = resList[0]
    res12 = resList[1]
    res23 = resList[2]
    resW = resList[3]

    # Place the saved elements in the list.
    save01 = saveList[0]
    save12 = saveList[1]
    save23 = saveList[2]
    saveW = saveList[3]

    # Set ratio from result and saved.
    ratio01 = res01/save01
    ratio12 = res12/save12
    ratio23 = res23/save23

    # Control the finger 1 servo motors.

    # Method1: Find degrees from the radians of two sides.
    if -1 <= ratio23 <= 1:               # Condition of arccos.
        radian = math.acos(ratio23)      # Find the radian value from the two sides.
        degree = 180 / math.pi * radian  # Find the degree value from the radian.
        print(degree)                    # If degree is not more then about 10, bc, ex) pixel distance 46/47 == 0.97. Less then 10 has to 0.99.

    # Method2: Find degrees from the ratio of original distance and degrees.
    # if (ratio23 - 10 <= ratio01 <= ratio23 + 10) and (ratio23 - 10 <= ratio12 <= ratio23 + 10):
    #     degree0123 = 90 * ratio23
    #     if degree0123 >= 0:
    #         pwmVal = round(pwm.servo_90 + (pwm.servo_0 - pwm.servo_180) / 180 * (90 - degree0123))
    #         pwm.device.set_pwm(0, 0, pwm.servo_90)
    #         pwm.device.set_pwm(1, 0, pwm.servo_90)
    #         pwm.device.set_pwm(2, 0, pwmVal)
    #     else:
    #         pwm.device.set_pwm(0, 0, pwm.servo_90)
    #         pwm.device.set_pwm(1, 0, pwm.servo_90)
    #         pwm.device.set_pwm(2, 0, pwm.servo_0)
