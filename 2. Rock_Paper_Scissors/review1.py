# 自行練習試題: 五行相剋相生進階運算
# 五行元素: 金、木、土、水、火，有相生與相剋的概念，
#   --> 金剋木、木剋土、土剋水、水剋火、火剋金；金生水、水生木、木生火、火生土、土生金

import random

my = int(input("請輸入元素 0.金 1.木 2.土 3.水 4.火:"))
com = random.randint(0, 4)
element = ["金", "木", "土", "水", "火"]
print("我選的元素: ", element[my])
print("電腦選的元素: ", element[com])

if my == (com + 1) % 5:
    print("我輸了")
elif com == (my + 1) % 5:
    print("我贏了")
elif my == (com + 3) % 5:
    print("反相生")
elif com == (my + 3) % 5:
    print("相生")
else:
    print("無勝負")