# 課程筆記
# 1. 記憶型迴圈，需要記憶的變數需要設在迴圈外面。

# title: Loop memory sample
# 計算"10?"階加，也就是計算1+2+3+...+10=多少?
total = 0
i = 0
while i < 10:
    total = total + (i + 1)
    # 第一次

    print(total)
    i += 1
print("!!!", total)