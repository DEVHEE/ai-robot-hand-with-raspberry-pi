"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""

# Import custom modules.
import modules.pca9685 as pca9685

output_file = "./text_output.txt"

# Read saved output file.
with open(output_file, "r") as f:
    lines = f.read().splitlines()
last_line = lines[-1:][0]  # Get last line.

print("DETECTED SPEECH:", last_line)

# Start speech movement process.
pca9685.speech(last_line)
