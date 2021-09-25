/*
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
*/

// Global variables and definition.
#define PWMPIN P1_0

unsigned char pwm_width;
bit pwm_flag = 0;

void pwm_setup()
{
    TMOD = 0;
    pwm_width = 160;
    EA = 1;
    ET0 = 1;
    TR0 = 1;
}

// Timer 0 Interrupt service routine.
void timer0() interrupt 1
{
    if (!pwm_flag)
    {                    // Start of High level.
        pwm_flag = 1;    // Set flag.
        PWMPIN = 1;      // Set PWM o/p pin.
        TH0 = pwm_width; // Load timer.
        TF0 = 0;         // Clear interrupt flag.
    }
    else
    {                          // Start of Low level.
        pwm_flag = 0;          // Clear flag.
        PWMPIN = 0;            // Clear PWM o/p pin.
        TH0 = 255 - pwm_width; // Load timer.
        TF0 = 0;               // Clear Interrupt flag.
    }
}

void pwm_stop()
{
    TR0 = 0; // Disable timer to disable PWM.
}