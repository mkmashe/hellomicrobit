from microbit import *

# ------------------
# ボタン
# ------------------

# sleep(10000)
# display.scroll(str(button_a.get_presses()))

# ------------------
# イベントループ
# ------------------
while running_time() < 5000:
    display.show(Image.ASLEEP)

display.show(Image.SURPRISED)

# ------------------
# イベントループ　２
# ------------------
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break
    else:
        display.show(Image.SAD)

display.clear()

