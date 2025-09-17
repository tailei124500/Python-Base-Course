a, b = 2, 5
print("初始", a, ",", b)

c = a
a = b
b = c
print(a, ",", b)

a, b = 2, 5
a = a + b
b = a - b
print(a, ",", b)

a, b = 2, 5
a = b
b = a
print(a, ",", b)

a, b = 2, 5
a, b = b, b
print(a, ",", b)

a, b = 2, 5
a, b = b, a
print(a, ",", b)