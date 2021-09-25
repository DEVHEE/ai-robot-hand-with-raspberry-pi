"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

# Import time module for delay.
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
# import logging
# logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
# pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths.
servo_min = 80  # Min pulse length out of 4096.
servo_max = 490  # Max pulse length out of 4096.

# for 60 Hz
# servo_min = 90  # Min pulse length out of 4096.
# servo_max = 590  # Max pulse length out of 4096.

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 50       # 50 Hz
    # pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 50 Hz.
pwm.set_pwm_freq(50)

# Set frequency to 60 Hz.
# pwm.set_pwm_freq(50)

print('Moving servo on channel 0...')
while True:
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)