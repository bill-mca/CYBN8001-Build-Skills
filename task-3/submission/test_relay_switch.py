import board
import digitalio
import time

relay = digitalio.DigitalInOut(board.A1)
relay.direction = digitalio.Direction.OUTPUT

while True:
    relay.value = True
    time.sleep(4)
    relay.value = False
    time.sleep(3)