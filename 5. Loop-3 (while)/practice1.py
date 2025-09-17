# 除法運算練習: 3 / 5

a, b = 3, 8
ans = "0."
i = 0
while i < 10:
    dividend = a * 10
    ans = ans + str(dividend // b)
    a = dividend % b
    if a == 0:
        print(ans)
        break
    i += 1