import speech

# speech.say("Hello, World")

# speech.say("I am a DALEK - EXTERMINATE", speed=120, pitch=100, throat=100, mouth=200)

# ------------------
# 音声　詩の朗読
# ------------------
# DALEK の本日のレース結果の自動作成プログラム
import speech
import random
from microbit import sleep

# random.seed(10)
# テンプレートに挿入する断片をランダムに選びます
race_number = random.choice(["nine", "ten", "eleven", "twelve"])
winner = random.choice(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])

# レポートのテンプレート。名前をつけた断片で {} を置き換えます
report = [
    "race report by computer voice",
    "race number {}".format(race_number),
    "winner is {}".format(winner),
    "thank you",
]

# ループでlistの各行を先頭から見て行き、speech モジュールを使って暗唱します
for line in report:
    speech.say(line, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)

# ------------------
# 音素 micro:bitの歌を歌う
# ------------------
# import speech
# from microbit import sleep
#
# # say メソッドは英語から音素への変換を試みます。
# speech.say("I can sing!")
# sleep(1000)
# speech.say("Listen to me!")
# sleep(1000)
#
# # throat をクリーンにするには音素を使う必要があります。
# # pitch と speed を変更することでも適切な効果が得られます。
# speech.pronounce("AEAE/HAEMM", pitch=200, speed=100)  # えへん
# sleep(1000)
#
# # 歌わせるには各音節ごとに音階の音素が必要です。
# solfa = [
#     "#115DOWWWWWW",   # ド
#     "#103REYYYYYY",   # レ
#     "#94MIYYYYYY",    # ミ
#     "#88FAOAOAOAOR",  # ファ
#     "#78SOHWWWWW",    # ソ
#     "#70LAOAOAOAOR",  # ラ
#     "#62TIYYYYYY",    # シ
#     "#58DOWWWWWW",    # ド
# ]
#
# # 音階が順に高くなっていくよう歌わせます。
# song = ''.join(solfa)
# speech.sing(song, speed=100)
# # 音節のリストの順番を逆にします。
# solfa.reverse()
# song = ''.join(solfa)
# # 音階が順に低くなっていくよう歌わせます。
# speech.sing(song, speed=100)