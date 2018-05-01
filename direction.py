from microbit import *

# ------------------
# 方向の検知
# ------------------
compass.calibrate() # コンパスの調整

while True:
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])
