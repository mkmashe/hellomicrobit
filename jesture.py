from microbit import *

while True:
    g = accelerometer.current_gesture()
    if g == "right":
        display.show(Image.ARROW_E)
    elif g == "left":
        display.show(Image.ARROW_W)
    elif g == "up":
        display.show(Image.ARROW_S)
    elif g == "down":
        display.show(Image.ARROW_N)
    else:
        display.show(Image.HAPPY)
