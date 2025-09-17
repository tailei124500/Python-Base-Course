# 自行練習試題: 終極密碼進階版(多輪遊戲選擇，使用雙層while迴圈)
import random

upper_limit, lower_limit = 100, 1
ans = random.randint(lower_limit + 1, upper_limit - 1)
guess_count = 0
round_count = 1
i = 0

game_round = int(input("請輸入要玩幾輪遊戲:"))

while i < game_round:
    upper_limit, lower_limit = 100, 1
    ans = random.randint(lower_limit + 1, upper_limit - 1)
    guess_count = 0
    print("___第", round_count, "輪遊戲___")
    round_count += 1
    i += 1

    while True:
        print("密碼介在", lower_limit, "~", upper_limit, "之間")
        guess = int(input("請輸入密碼:"))

        if guess > ans:
            upper_limit = guess
            guess_count += 1
            print("再小一點~")
        
        elif guess < ans:
            lower_limit = guess
            guess_count += 1
            print("再大一點~")

        else:
            guess_count += 1
            print("恭喜答對!!!", "總共猜了", guess_count, "次~")
            break

# 以下為ChatGPT改善範例:

"""
import random

game_round = int(input("請輸入要玩幾輪遊戲: "))
round_count = 1
results = []  # 用來存放每輪的猜測次數

while round_count <= game_round:
    upper_limit, lower_limit = 100, 1
    ans = random.randint(lower_limit + 1, upper_limit - 1)
    guess_count = 0

    print(f"\n___ 第 {round_count} 輪遊戲 ___")

    while True:
        try:
            guess = int(input(f"請輸入數字 ({lower_limit} ~ {upper_limit}): "))
        except ValueError:
            print("⚠ 輸入錯誤，請輸入整數！")
            continue

        if not (lower_limit < guess < upper_limit):
            print("⚠ 數字不在範圍內，請重新輸入！")
            continue

        guess_count += 1
        if guess > ans:
            upper_limit = guess
            print("再小一點~")
        elif guess < ans:
            lower_limit = guess
            print("再大一點~")
        else:
            print(f"🎉 恭喜答對！總共猜了 {guess_count} 次~")
            results.append(guess_count)
            break

    round_count += 1

# 遊戲總結
print("\n📊 遊戲結束！各輪成績：")
for i, r in enumerate(results, 1):
    print(f"第 {i} 輪：{r} 次")
print("平均猜測次數：", sum(results) / len(results))
"""

# 改善重點:
"""
1. 輸入檢查（避免輸入錯誤直接壞掉）
    a. 原本程式沒有檢查「輸入是否為整數」或「是否在範圍內」。
    b. 如果玩家輸入字串（例如 abc）或超出範圍（例如 200），程式就會錯誤或邏輯怪怪的。
        --> 可以加上 try-except 或判斷式 if lower_limit < guess < upper_limit:。

2. 統計成績
    a. 題目要求最後顯示「每輪猜測次數」與「平均值」。
    b. 原本程式只有在每一輪結束時顯示次數，但沒有統計全部的成績。
        --> 可以用一個 list 來存放每輪的猜測次數，最後再統計平均。

3. 程式碼更結構化
    a. i 和 round_count 其實功能重疊（都是記錄第幾輪）。
    b. 可以直接用 for 回合 in range(1, game_round+1): 或者單純用 round_count，減少變數。
        --> 但因題目特別要求「使用 while」，所以保留 while 沒問題，但 round_count 一個變數就足夠。    
"""