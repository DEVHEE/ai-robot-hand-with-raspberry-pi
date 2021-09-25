"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

# Import Raspberry Pi GPIO module to use GPIO.
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Set pin index for signal to servo motor.
signalPin = 16

GPIO.setup(signalPin, GPIO.OUT)

pwm = GPIO.PWM(signalPin, 50)

# Init value.
pwm.start(7)

for i in range(0, 20):
    pos=input("Select degrees 0-180: ")
    DC = 1./18.*(pos)+2
    pwm.ChangeDutyCycle(DC)
    
pwm.stop()
GPIO.cleanup()