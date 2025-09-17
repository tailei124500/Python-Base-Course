# 進階練習題: 成績分析系統
# 有一個班級三次考試的分數，存成一個二維list，如下:
# scores = [
#     [80, 60, 90, 20, 100],   # 第一次考試
#     [70, 85, 55, 40, 95],    # 第二次考試
#     [88, 77, 66, 99, 50]     # 第三次考試
# ]

# 請用while迴圈+list，完成以下功能：
# 1. 計算每次考試的平均分數。
#   --> (提示: 用sum()和len()或while迴圈累加)
# 2. 計算每位同學的平均分數，並印出「第X位同學: 平均Y分」。
# 3. 找出三次考試中「最高分」與「最低分」各是多少。
# 額外挑戰：
#   --> a. 列出「及格次數最多」的同學（例如某同學三次都及格，他就是最強）。
#   --> b. 把每次考試的分數反轉印出（練習 [::-1]）。

scores = [
    [80, 60, 90, 20, 100],   # 第一次考試
    [70, 85, 55, 40, 95],    # 第二次考試
    [88, 77, 66, 99, 50]     # 第三次考試
]

quiz_count_len = len(scores) # 3
first_len = len(scores[0]) # 5
second_len = len(scores[1]) # 5
third_len = len(scores[2]) # 5
total_len = len(scores[0]) + len(scores[1]) + len(scores[2]) # 15
# 使用「total_len = sum(map(len, scores))」寫法，於scores list隨意增加Element時，較不會出現問題
#   --> map(function, iterables)，假設total_len2 = map(len, scores)，print(list(total_len2))會印出[5, 5, 5]

# 1. 計算每次考試的平均分數
# i = 0
# scores_sum = 0

# while i < quiz_count_len:
#     scores_sum = sum(scores[i])
#     print("第", (i + 1), "次考試平均分數為：", scores_sum / len(scores[i]))
#     i += 1

# 2. 計算每位同學的平均分數，並印出「第X位同學: 平均Y分」
# i = 0

# while i < int(total_len / quiz_count_len):
#     classmate_scores_sum = 0
#     j = 0
#     while j < quiz_count_len:
#         classmate_scores_sum += scores[j][i]
#         j += 1
#     print("第", (i + 1), "位同學平均分數為：", classmate_scores_sum / quiz_count_len)
#     # 若要將平均分數只顯示小數點第二位，可改為使用以下程式碼:
#     # print(f"第{i + 1}位同學平均分數為：{classmate_scores_sum / quiz_count_len:.2f}")
#     i += 1

# 3. 找出三次考試中「最高分」與「最低分」各是多少
# i = 0

# while i < quiz_count_len:
#     print(f"第{i + 1}次考試最高分數為:{max(scores[i])}，最低分數為:{min(scores[i])}。")
#     i += 1

# 額外挑戰 a. 列出「及格次數最多」的同學
# 先計算所有同學在三次考試中的總及格次數
i = 0
pass_count = [0] * int(total_len / quiz_count_len) # 因為要計算次數的scores為list，故需創建一個對應型態的list來記錄次數

while i < int(total_len / quiz_count_len):
    j = 0
    while j < quiz_count_len:
        if scores[j][i] >= 60:
            print(f"編號為{i}的同學，第{j + 1}次考試成績為:{scores[j][i]}")
            pass_count[i] += 1 
            # 若判斷的分數大於等於60，則依序將pass_count[0, 0, 0, 0, 0]內的Element + 1，用來計算每位同學在三次考試中的總及格次數
            print(f"所以在pass_count list內，編號為{i}的同學增加一次及格次數:\n{pass_count}\n")
        else:
            pass
        j += 1
    i += 1

# 接著按照所有同學在三次考試中的總及格次數來選出「及格次數最多」的同學
k = 0 # 不同組迴圈建議建立新的迴圈計數器，增加可讀性
max_pass = max(pass_count)

while k < len(pass_count):
    if pass_count[k] == max_pass:
        print(f"編號為{k}的同學，及格次數最高，且為{max_pass}次")
    else:
        pass
    k += 1

# 額外挑戰 b. 把每次考試的分數反轉印出
# i = 0

# while i < quiz_count_len:
#     print(scores[i][::-1])
#     i += 1

# 練習題目重點筆記:     
# 1. 使用雙層while迴圈逐層拆解二維list並按照由左至右、由上至下的順序印出
# while i < quiz_count_len:
#     j = 0
#     # print(scores[i]) # 印出scores中第一層list
#     while j < int(total_len / quiz_count_len):
#         # print(scores[i][j]) # 拆解二維list，並逐層按照順序印出scores中所有單個Element，
#         j += 1
#     i += 1

# 2. 使用雙層while迴圈逐層拆解二維list，先按照由上至下、再由左至右的順序印出每個Element(類似轉置)
#   --> 快速記法: 若要轉置印出二維list，程式碼架構與上述情況相同，
#   --> 僅需交換內外層whlie迴圈條件的值，以及交換print函式內list的順序([i][j] -> [j][i])
# i = 0
# classmate_scores_sum = 0

# while i < int(total_len / quiz_count_len):
#     j = 0
#     while j < quiz_count_len:
#         print(scores[j][i])
#         j += 1
#     i += 1