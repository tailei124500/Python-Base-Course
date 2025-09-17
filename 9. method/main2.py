# 課程筆記
# 1. append()函式用於將元素加入變數的尾端，Syntax: list.append(elmnt)
# 2. insert()函式用於將元素加入變數的指定位置，
# 3. pop()函式用於移除變數中指定位置的元素

scores = [50, 40, 60]

b = scores.append(99)  # 將99加入scores的尾端，且append()函式沒有回傳值，而是直接改變scores
print(scores) # 所以印出scores會得到[50, 40, 60, 99]
print(b) # 因為append()沒有回傳值，印出b會得到None

# 4. 四大基礎型態
#   --> 1. 數字型態: 包含整數(int)和浮點數(float)
#   --> 2. 字串型態: 用雙引號定義，e.g. "hello"
#   --> 3. 布林型態: 只有True和False兩個值
#   --> 4. None型態: 代表沒有值或空值

# 5. 回傳值概念顛覆
#   --> 以前，有些功能有回傳值，e.g. int()、input()；有些功能沒有回傳值，e.g. print()
#   --> 現在，任何功能都有回傳值，只是有些功能回傳None而已
print(print(print(4.2))) # 印出4.2，然後印出None兩次，因為print()只回傳None

# 6. 顛覆點2.Value的改變
#   --> 以前，"="等號若沒有設置，Value就永遠不變
#   --> 現在，有時Value會直接改變，譬如list的專屬功能(method)

# 字串專屬功能: print(s.replace(xxx, ooo))
# 錯誤示範1:
# print(scores.append(888)) 
# 上式將888加入scores的尾端，但因為print()只回傳None，所以印出None，但scores已經變成[50, 40, 60, 99, 888]

# 錯誤示範2:
# 字串: s = s.replace()，相當於寫scores = None
# scores = scores.append(777)
# print(scores[-1]) 
# # 因為print(scores.append(777))只回傳None，所以print(scores[-1])會出現錯誤

# 正確示範:
scores.append(1234)
print(scores)
print(scores[-1])

# SOP
# 字串型的method: b = a.replace()，這時a是舊字串，b是新字串
# 清單型的method: b = a.append()，這時a是新清單，b是None
# 分辨方法: 直接嘗試print，如果印出None，則是清單型的method