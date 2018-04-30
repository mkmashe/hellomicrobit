from microbit import *

while True:
    for b in range(0, 10):
        for x in range(0, 5):
            for y in range(0, 5):
                display.set_pixel(x, y, (x+y+b) % 10)
        sleep(20)
