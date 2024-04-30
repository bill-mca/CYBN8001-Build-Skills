
"""
Stork

This code animates a tork that will threaten an axolotl and cause it to spray water when approached
The axolotl is a specific Bluefruit device that is monitoring BLE advertisements.
The stork broadcastssignal for the axolotl to detect.
"""

import time
from adafruit_circuitplayground.bluefruit import cpb

from adafruit_ble import BLERadio
from adafruit_ble.advertising.adafruit import AdafruitColor

stork = 'CIRCUITPY7d29'
axolotl =

ble = BLERadio()


while True:

    print("Scanning for devices")
    cpb.pixels.fill(0x111111)
    advertisements = ble.start_scan(minimum_rssi=-200, timeout=0.3)
    ads = [(e.complete_name, e.rssi) for e in advertisements]
    ble.stop_scan()
    names = [x for x, y in ads]
    rssis = [y for x, y in ads]
    #print(names)
    #print(stork in names)
    if stork in names:
        stork_rssi = rssis[names.index(stork)]
        print('stork rssi: ', stork_rssi)
        # This discrete strength code was taken from an Adafruit tutorial
        # 2019 John Edgar Park for Adafruit Industries MIT licence
        discrete_strength = min((100 + stork_rssi) // 5, 10)
        for i in range(0, discrete_strength):
            cpb.pixels[i] = 0x110000
        cpb.pixels.show()
        #if stork_rssi < 70:
        #  spray water
        #elif stork rssi < 80:
        #   warn the user
    time.sleep(3)