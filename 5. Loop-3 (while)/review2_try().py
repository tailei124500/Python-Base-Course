# try()函式練習

# 1. 數字輸入驗證
#   --> 輸入一個整數，並嘗試把它轉換為int，如果輸入的不是整數，提示「請輸入正確的數字！」
#   --> 如果輸入成功，就印出「輸入的數字是 X」。

"""
try:
    x = int(input("請輸入一個整數:"))
    print("輸入的數字是:", x)

except ValueError:
    print("請輸入正確的數字！")
"""

# 2. 除法運算
#   --> 輸入兩個數字，並進行除法。
#   --> 如果輸入不是數字，提示「輸入錯誤，請輸入數字！」
#   --> 如果除數為 0，提示「除數不能為 0！」
#   --> 否則印出「結果為：X」。

"""
try:
    x = float(input("請輸入第一個數字:"))
    y = float(input("請輸入第二個數字:"))
    print("結果為:", x / y) # 使用「print(f"結果為: {x / y:.2f}")」可取到小數點兩位，避免浮點數雜亂顯示


except ValueError:
    print("輸入錯誤，請輸入數字！")

except ZeroDivisionError:
    print("除數不能為0！")
"""

# 3. 檔案讀取
#   --> 嘗試開啟一個檔案 test.txt，讀取內容並印出。
#   --> 如果檔案不存在，請提示「找不到檔案！」。
#   --> 如果讀取成功，印出檔案內容。
# 提示：用 open("test.txt", "r") 並搭配 try / except FileNotFoundError。

try:
    file = open("test.txt", "r", encoding="utf-8")
    print(file.read())

except FileNotFoundError:
    print("找不到檔案！")

finally:
    file.close()