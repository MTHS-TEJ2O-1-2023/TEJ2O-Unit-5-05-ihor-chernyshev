"""
Created by: Ihor Chernyshev
Created on: Oct 2023
This program uses the RobotBit's Neopixels to create Traffic Light
"""

# setup
from microbit import *
import neopixel

display.clear()
np = neopixel.NeoPixel(pin16, 4)
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np[3] = (0, 0, 0)
np.clear()
display.show(Image.HAPPY)

while True:
    # turning on green
    np[2] = (0, 255, 0)
    print(np[2])
    np.show()
    sleep(1000)
    np.clear()

    # turning on yellow
    np[1] = (255, 255, 0)
    print(np[1])
    np.show()
    sleep(1000)
    np.clear()

    # turning on red
    np[0] = (255, 0, 0)
    print(np[0])
    np.show()
    sleep(1000)
    np.clear()
