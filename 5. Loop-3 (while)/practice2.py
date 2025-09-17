# 終極密碼
# 條件為「下限: 1，答案: 50，上限: 100」，
#   --> 如果第一次猜80，條件會變為「下限: 1，答案: 50，上限: 80」
#   --> 如果第二次猜30，條件會變為「下限: 30，答案: 50，上限: 80」

import random

upper_limit, lower_limit = 100, 1
answer = random.randint(lower_limit + 1, upper_limit - 1)

while True:
    guess = int(input("請輸入數字(限" + 
                      str(lower_limit) + 
                      "~" + 
                      str(upper_limit) + 
                      "之間): "))
    if guess > upper_limit or guess < lower_limit:
        print("輸入錯誤!!! 請重新執行~")
        break
    
    elif guess == answer:
        print("恭喜答對!!!")
        break

    elif guess > answer:
        upper_limit = guess
        print("再低一點...")
    
    elif guess < answer:
        lower_limit = guess
        print("再高一點...")