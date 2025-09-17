# 課程筆記
# 其他條件迴圈
# 1. Loop-1/2皆為次數條件的迴圈，但迴圈的使用上不一定只有次數條件。
# 2. 程式語言皆有四大基礎型態: 1.數字 2.字串 3.布林(True/False) 4.無(None)
# 3. 布林(Boolean)型態只有兩種值: Ture/False。
# 4. 只要在函式加上"not"即為"不"的意思，e.g. "if not bmi > 18:"
#   --> 意思為"如果bmi沒有 > 18"，也就是說"bmi <= 18"的意思
# 5. 組合有兩種，"而且(and)"和"或者(or)"。
# 6. 無窮迴圈:
#   --> 如果寫"while 2 > 5"，一次都不會做，因為永遠是錯的。
#   --> 寫法: "while False"，幾乎不會用到。
#   --> 如果寫"while 5 > 2"，會做無限次，因為永遠是對的。
#   --> 寫法: "while Ture"，但不可能無限做下去，會搭配"break"做結束。
# 7. 若"while"函式的條件非常複雜或是不知道該寫甚麼，可以考慮使用"while True"加上"break"，
#   --> 使用上會非常自由，複雜的判斷可以放在"while"函式之後，並且隨時使用"break"結束。

# title: title: Rock Paper Scissors Game (Advance)
import random

win, lose = 0, 0

while win < 3 and lose < 3:
    # -1: lose, 0: even, 1: win
    result = random.randint(-1, 1)
    print(result)

    if result == -1:
        lose += 1
    elif result == 1:
        win += 1
if win > lose:
    print("I Win !")
else:
    print("I Lose !")

# while迴圈更適合的寫法
win, lose = 0, 0

while True:
    # -1: lose, 0: even, 1: win
    result = random.randint(-1, 1)
    print(result)

    if result == -1:
        lose += 1
    elif result == 1:
        win += 1

    # 判斷
    if win == 3:
        print("I Win !")
        break
    elif lose == 3:
        print("I Lose !")
        break