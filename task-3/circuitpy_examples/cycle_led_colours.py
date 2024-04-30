
import time
from adafruit_circuitplayground.bluefruit import cpb
#from adafruit_circuitplayground import cp

# The color pickers will cycle through this list with buttons A and B.
# color_options = [0x110000,
#                  0x111100,
#                  0x001100,
#                  0x001111,
#                  0x000011,
#                  0x110011,
#                  0x111111,
#                  0x221111,
#                  0x112211,
#                  0x111122]
#
# def fill_pixels(cp, discrete_strength):
#     cp.pixels.fill(0x000000)
#     # The range seems to be about -40 (close) to -100 (far)
#     print(entry.rssi)
#     for i in range(0, discrete_strength):
#         cp.pixels[i] = entry.color
#     cp.pixels.show()

while True:
    x, y, z = [abs(x) for x in cpb.acceleration]
    top_speed = max([x,y,z])
    print(top_speed)
    #fill_pixels
    cpb.pixels.fill((x,y,z))
