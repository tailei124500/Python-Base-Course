a, b = 60, 48

while True:
    if b == 0:
        print("這個神秘數字是:", a)
        break
    a, b = a % b, b
    a, b = max(a, b), min(a, b)