from microbit import *
import music

# ------------------
# 動きの検知
# ------------------
# while True:
#     reading = accelerometer.get_x()
#     if reading > 70:
#         display.show("R")
#     elif reading < -70:
#         display.show("L")
#     else:
#         display.show("-")

# ------------------
# 傾きを音で表現 
# ------------------
while True:
    music.pitch(accelerometer.get_x(), 10)