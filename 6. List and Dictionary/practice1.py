# 以下為全班人的考試分數，試計算幾個人及格，並使用迴圈
# 考試分數: 80, 60, 90, 20, 100

scores = [80, 60, 90, 20, 100]
pass_count = 0

i = 0
while i < len(scores):
    if scores[i] >= 60:
        pass_count += 1
    i += 1

print(pass_count)

# 在後續群集的狀況下，清單變數[key]中的key不一定會按照順序由0, 1, 2, 3,..., n排列
#   --> 故以上程式碼是不夠泛用的。