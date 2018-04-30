from microbit import *

while True:
    # image = Image("99999:99999:99999:99999:99999")

    # -----
    # tan
    # -----
    ta = Image("99999:90909:99999:90909:99999")
    naka = Image("00900:99999:90909:99999:00900")

    # -----
    # dem
    # -----
    de = Image("90909:99999:00900:90909:99999")
    machi = Image("99900:95999:99909:95909:99909")

    # -----
    # kaw
    # -----

    kawa = Image("90999:09999:99909:09999:90009")
    mura = Image("09009:99999:09909:99009:09099")

    kanji_list = [ta, naka, de, machi, kawa, mura]

    # for i in range(0,6):
    #     display.show(kanji_list[i])
    #     if i % 2 == 0:
    #         sleep(1000)
    #     else:
    #         sleep(2000)

    # １行で書ける
    display.show(kanji_list, delay=1000)
