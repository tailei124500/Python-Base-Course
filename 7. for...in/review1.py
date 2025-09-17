# 進階練習題: 九九乘法表分析
# 使用for...in與range()，完成以下功能：
# 1. 印出九九乘法表（格式：2 x 3 = 6）。
# 2. 計算所有乘積的總和。
# 3. 計算乘積為偶數的次數與奇數的次數。

print("1. 印出九九乘法表")
product_sum = 0
odd, even = 0, 0 # 奇數: odd number，偶數: even number

for i in range(9):
    for j in range(9):
        print(f"{i + 1} x {j + 1} = {(i + 1) * (j + 1)}") # 印出九九乘法表
        
        product_sum += (i + 1) * (j + 1) #  計算所有乘積的總和，迴圈外印出結果
        
        # 計算乘積為偶數的次數與奇數的次數，迴圈外印出結果
        if (i + 1) * (j + 1) % 2 == 0:
            even += 1
        elif (i + 1) * (j + 1) % 2 == 1:
            odd += 1

print(f"\n2. 九九乘法表所有的乘積總和為:{product_sum}")
print(f"\n3. 乘積為奇數的次數為:{odd}，乘積為偶數的次數為:{even}")

# 此部分程式碼為針對題目分開撰寫
# 1. 印出九九乘法表
# print("1. 印出九九乘法表")

# for i in range(9):
#     for j in range(9):
#         print(f"{i + 1} x {j + 1} = {(i + 1) * (j + 1)}")

# 2. 計算所有乘積的總和
# product_sum = 0

# for k in range(9):
#     for l in range(9):
#         product_sum += (k + 1) * (l + 1)

# print(product_sum)

# 3. 計算乘積為偶數的次數與奇數的次數
# odd, even = 0, 0 # 奇數: odd number，偶數: even number

# for m in range(9):
#     for n in range(9):
#         # print((m + 1) * (n + 1))
#         if (m + 1) * (n + 1) % 2 == 0:
#             even += 1
#         elif (m + 1) * (n + 1) % 2 == 1:
#             odd += 1

# print(odd, even)