# 自行練習試題: 隨機漫步(Random Walk)模擬
# 一隻螞蟻站在座標 (0, 0)，每次隨機選擇一個方向（上 U、下 D、左 L、右 R），一步的距離 = 1。
# 請使用 while 迴圈模擬螞蟻走路，並完成以下任務：
#   --> 輸入 step（總步數），模擬螞蟻走完這些步數後的最終座標。
#   --> 印出螞蟻的完整路徑（每一步的座標）。
#   --> 額外挑戰：計算螞蟻與原點 (0,0) 的「最遠直線距離」。

import random
import math # 用於計算最遠直線距離(畢氏定理)，開根號"math.sqrt()"

x, y = 0, 0
step = int(input("請輸入總步數:"))
i = 0
max_dis = 0

print("你輸入的總步數為:", step)

while i < step:
    R = random.randint(0, 1)
    L = random.randint(0, 1)
    U = random.randint(0, 1)
    D = random.randint(0, 1)
    if R == 1 and L == 0 and U == 0 and D == 0:
        x += 1
    elif R == 0 and L == 1 and U == 0 and D == 0:
        x -= 1
    elif R == 0 and L == 0 and U == 1 and D == 0:
        y += 1
    elif R == 0 and L == 0 and U == 0 and D == 1:
        y -= 1
    else:
        continue 
    # 此段if寫法較耗費計算資源，因為非上述四種條件的運算都會被continue掉
    #   --> 可改用direction = random.choice(["R", "L", "U", "D"])函式(ChatGPT建議)
    #   --> 隨機選出方向再進行對照的步數疊加運算

    i += 1
    print("第", i, "步移動，", "R:", R, "L:", L, "U:", U, "D:", D) # 該項若放在"i += 1"之前，要寫成「"第", i + 1, "步移動，"」
    print("現在位置:", "(", x,",", y, ")")

    dis = float(math.sqrt(abs(x) ** 2 + abs(y) ** 2))
    print("目前位置與原點的距離為:", dis)

    if dis > max_dis:
        max_dis = dis

print("與原點的最遠直線距離為:", max_dis)

"""
補充:
1. break: 強制跳出"整個"迴圈
2. continue: 強制跳出"本次"迴圈，繼續進入下一圈
3. pass: 不做任何事情，所有的程式都將繼續
"""

# 以下為ChatGPT提供的程式碼:

"""
import random
import math

# 初始位置
x, y = 0, 0

# 記錄最遠距離
max_dist = 0

# 設定步數
steps = 1000
count = 0

while count < steps:
    # 隨機決定方向
    direction = random.choice(['N', 'S', 'E', 'W'])

    if direction == 'N':   # 向北
        y += 1
    elif direction == 'S': # 向南
        y -= 1
    elif direction == 'E': # 向東
        x += 1
    else:                  # 向西
        x -= 1

    # 計算目前距離原點的距離
    dist = math.sqrt(x**2 + y**2)

    # 更新最遠距離
    if dist > max_dist:
        max_dist = dist

    count += 1

print(f"最遠距離: {max_dist:.2f}")    
"""