"""
ai-robot-hand-with-raspberry-pi
COPYRIGHT © 2021 KIM DONGHEE. ALL RIGHTS RESERVED.

watson-streaming-stt
COPYRIGHT © 2016 IBM. ALL RIGHTS RESERVED.
"""

# Import modules.
import setuptools

try:
    import multiprocessing  # noqa
except ImportError:
    pass

setuptools.setup(
    setup_requires=['pbr>=1.8'],
    pbr=True)
