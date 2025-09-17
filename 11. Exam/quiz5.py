total = 0
n = 12345

while n > 0:
    total = total + (n % 10)
    n = n // 10
    
print(total)