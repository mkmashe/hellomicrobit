from microbit import *
import random

# ------------------
# ランダム 
# ------------------

# names = ["Mary", "Yolanda", "Damien", "Alia", "Kushal", "Mei Xiu", "Zoltan"]
# 
# display.scroll(choice(names))

# display.show(str(random.randint(1, 6)))

random.seed(1337)
while True:
    if button_a.was_pressed():
        display.show(str(random.randint(1, 6)))
