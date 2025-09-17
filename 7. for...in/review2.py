# 進階練習題: 使用for...in迴圈分析巢狀list
# 1. 計算每個學生的平均分數，並依序輸出。
# 2. 計算全班的總平均分數 (提示: 可以先把所有分數展開成一個大list，或用巢狀迴圈加總)。
# 3. 挑戰題: 找出全班的「最高分」與「最低分」，並輸出是哪位學生的第幾科。

scores = [
    [80, 75, 92],   # 學生 A 的成績
    [60, 65, 70],   # 學生 B 的成績
    [90, 95, 88],   # 學生 C 的成績
]

student = ["A", "B", "C"]

# 1. 計算每個學生的平均分數，並依序輸出。
# for i in range(len(scores)):
#     print(f"學生{student[i]}的平均分數為:{sum(scores[i]) / len(scores):.2f}分")

# 2. 計算全班的總平均分數
# student_scores_sum = 0

# for k in range(len(scores)):
#     for l in range(int(sum(map(len, scores)) / len(scores))):
#     # list(map(len, scores)) == [3, 3, 3]，計算scores內第一層list的len，故sum(map(len, scores) == 9.0
#     #   --> 主要用於假設scores list會隨機增加的情況下，不需修改迴圈判斷式
#         student_scores_sum += scores[k][l]

# print(f"全班的總平均分數為(不分科):{student_scores_sum / int(sum(map(len, scores))):.2f}")

# for...in迴圈ChatGPT建議寫法: 
# for row in scores:
#     for val in row:
#         student_scores_sum += val
# 相較於使用舊方法較不易出錯，若未來不同學生科目數不同，也不需進行修改直接使用


# 3. 挑戰題: 找出全班的「最高分」與「最低分」，並輸出是哪位學生的第幾科。
max_score = 0
min_score = min(scores[0])

for m in range(len(scores)):
    for n in range(int(sum(map(len, scores)) / len(scores))):

        if scores[m][n] > max_score:
            max_score = scores[m][n]
            get_max_score_student, get_max_score_student_subject = m, n + 1

        if scores[m][n] < min_score:
            min_score = scores[m][n]
            get_min_score_student, get_min_score_student_subject = m, n + 1
        
print(f"""恭喜同學{student[get_max_score_student]}在科目{get_max_score_student_subject}拿到全班最高分:{max_score}。
另外同學{student[get_min_score_student]}在科目{get_min_score_student_subject}拿到全班最低分:{min_score}，請加油~""")

# print(f"""XX
# X""")
# 以上三個「"」包圍內容的使用方式，輸出會自動換行，也可增加程式碼可讀性