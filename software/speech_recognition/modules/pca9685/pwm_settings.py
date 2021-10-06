"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

# Import modules.
import time
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
device = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths.
servo_min = 80  # Min pulse length out of 4096.
servo_max = 490  # Max pulse length out of 4096.

# Configure 0, 90, 180 degrees of servo pulse lengths.
# 1 degree per 2.055
servo_180 = 100  # 180 degrees length out of 4096.
servo_135 = round(192.5)  # 135 degrees length out of 4096.
servo_90 = 285  # 90 degrees length out of 4096.
servo_45 = round(377.5)  # 45 degrees length out of 4096.
servo_0 = 470  # 0 degrees length out of 4096.


# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 50       # 50 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    device.set_pwm(channel, 0, pulse)


# Set frequency to 50 Hz.
device.set_pwm_freq(50)
