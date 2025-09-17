# 終極密碼
# 條件為「下限: 1，答案: 50，上限: 100」，
#   --> 如果第一次猜80，條件會變為「下限: 1，答案: 50，上限: 80」
#   --> 如果第二次猜30，條件會變為「下限: 30，答案: 50，上限: 80」

# Modify List
# 1. 原本撰寫的practice2.py執行上有一個缺點，如果輸入錯誤就會直接結束程式，而不是程式重新開始。
#   --> 改變撰寫的方向，將輸入錯誤的if函式拿到外部，內部才加入猜對或猜錯的if函式。
# 2. guess變數可以單獨拉出來，減少input函式的長度
# 3. 程式碼也可以再更改邏輯，先判斷使用者是否輸入錯誤，錯誤直接提示，
#   --> 輸入無錯再進入猜對或猜錯的if函式也可以。

import random

upper_limit, lower_limit = 100, 1
answer = random.randint(lower_limit + 1, upper_limit - 1)

while True:
    
    # 原版guess變數函式
    # guess = int(input("請輸入數字(限" + 
                      # str(lower_limit) + 
                      # "~" + 
                      # str(upper_limit) + 
                      # "之間): "))
    
    # 改成
    print("請輸入數字(限", lower_limit, "~", upper_limit, "之間): ")
    guess = int(input())

    # 原版if函式
    # if guess > upper_limit or guess < lower_limit:
        # print("輸入錯誤!!! 請重新執行~")
        # break
    
    # elif guess == answer:
        # print("恭喜答對!!!")
        # break

    # elif guess > answer:
        # upper_limit = guess
        # print("再低一點...")
    
    # elif guess < answer:
        # lower_limit = guess
        # print("再高一點...")

    # 改成
    if guess < upper_limit and guess > lower_limit:
    # 使用者輸入正確的數字範圍才會進入遊戲

        if guess > answer:
            upper_limit = guess
            print("再低一點...")
        elif guess < answer:
            lower_limit = guess
            print("再高一點...")
        else:  
            print("恭喜答對!!!")
            break
    
    else:
        print("輸入錯誤!!! 請重新執行~")

# 講師寫的
# import random

# lower_limit, upper_limit= 1, 100
# answer = random.randint(lower_limit + 1, upper_limit - 1)

# while True:
    # while True:
        # print("請輸入數字(限", lower_limit, "~", upper_limit, "之間): ")
        # guess = int(input())
        # if lower_limit < guess < upper_limit:
            # break
        # else:
            # print("輸入錯誤!!! 請重新執行~")
    
    # if guess == answer:
        # print("恭喜答對!!!")
        # break

    # elif guess > answer:
        # upper_limit = guess
        # print("再低一點...")
    
    # elif guess < answer:
        # lower_limit = guess
        # print("再高一點...")

# 將使用者輸入多使用迴圈來判斷，並使用break來跳脫該層判斷迴圈，程式碼更加模組化。