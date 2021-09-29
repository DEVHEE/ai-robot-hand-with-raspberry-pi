"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.
"""


# Function of calculate joint.
def calcJoint(joint1, joint2):
    calc = map(lambda x, y: map(lambda i, j: i-j, x, y), joint1, joint2)
    res = [tuple(i) for i in calc][0][1]
    return res
