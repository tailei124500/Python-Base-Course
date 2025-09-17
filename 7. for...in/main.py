# 課程筆記
# 1. 使用改進版的for...in (走過)來執行群集的迴圈
# 2. 函式架構: for 名稱 in 群集(str/list...):
# 3. 名稱中的內容會在for迴圈走過並取得群集的值而改變

# 接續 6. List and Dictionary - practice1.py的程式碼

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

# 使用for...in函式的對照範例
pass_count = 0
for score_sum in scores:
    if score_sum >= 60:
        pass_count += 1

print(pass_count)
# for迴圈走過scores[]，只要下方if函式按照順序(不再只是key=0, 1, 2, 3,..., n)判斷scores[]中的每個元素(走過)，
#   --> 有大於60的元素，就會在score_sum中自動記錄(+1)。

# 迴圈使用的SOP 重要!!! 重要!!! 重要!!!
# 1. 走過群集(str/list...): for 名稱 in 群
# 2. 固定次數迴圈: for i in range(次)
# 3. 其他條件迴圈: while (True + break)