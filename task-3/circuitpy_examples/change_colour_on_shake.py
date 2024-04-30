# Created by Tom Xu

from adafruit_circuitplayground import cp
import time
from random import randint

cp.pixels.brightness = 0.05
cp.pixels.fill((0, 255, 0))
cp.pixels.show()

leds_on = True

while True:
    print('Yeah!')
    if cp.shake(shake_threshold=15):
        leds_on = leds_on
        if leds_on:
            colour = (randint(0, 255), randint(0, 255), randint(0, 255))
            for i in range(10):
                cp.pixels[i] = (colour[0], colour[1], colour[2])
                cp.pixels.show()
                time.sleep(0.1)
        else:
            for i in range(10):
                cp.pixels[i] = (0, 0, 0)
                cp.pixels.show()
                time.sleep(0.1)

