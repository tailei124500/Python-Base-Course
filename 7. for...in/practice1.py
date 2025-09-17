# 改使用for...in迴圈計算1+2+3+...+10
# range函式: 產生類似list的型態，總共三種用法:
# 1. range(5)產生[0, 1, 2, 3, 4]
# 2. range(3,5)產生[3, 4]
# 3. range(2, 11, 3)產生[2, 5, 8](三個一跳)

total = 0
for i in range(10):
    total =  total + (i + 1)
    print(total)