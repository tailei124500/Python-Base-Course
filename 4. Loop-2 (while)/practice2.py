# 機器人移動運算
# 給機器人一連串指令(e.g. UDDLR)，計算機器人最後的位置在哪
# 機器人初始位置為(0, 0)，U: 上，D: 下，L: 左，R: 右

# len()函式: 算出字串變數的數量

x, y = 0, 0
commands = "ULLRDL"

i = 0
while i < len(commands):
    if commands[i] == "U":
        y = y + 1
    elif commands[i] == "D":
        y = y - 1
    elif commands[i] == "L":
        x = x - 1
    elif commands[i] == "R":
        x = x + 1

    print("(" + str(x) + ", " + str(y) + ")")
    i += 1