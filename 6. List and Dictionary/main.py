# 課程筆記

scores = [30, 50, 80, 60, 90]

# 清單基本使用方法
print(sum(scores), max(scores), min(scores)) # 清單的加總、最大、最小
print(len(scores)) # 清單的長度
print(60 in scores) # 搜尋清單內是否有該元素

# 1. 查詢操作: 清單變數[key]，其中"key"會從0開始，例如以上範例的清單key = 0會是30。
print(scores[0])

# 查詢清單的最後一個元素，len()會計算出總數量，因為key是從0開始，所以會再做-1的動作。
print(scores[len(scores)-1]) # 但此程式碼結構不夠漂亮(不夠Pythonic)

# 反向key
# scores = [30, 50, 80, 60, 90]
# 正向key，scores清單內的元素key分別會是"0"、"1"、"2"、"3"、"4"
# 反向key，scores清單內的元素key分別會是"-5"、"-4"、"-3"、"-2"、"-1"
# 反向key的最後一定是從"-1"開始!!!
print(scores[-1])

# 2. 若要查詢一段可以使用: 清單變數[開始key:結束key(不包含，也就是只會查詢到結束key前一個的意思)]
#   --> e.g. list[2:5]等於查詢list[2]、list[3]、list[4]
print(scores[1:3])

print(scores[1:-1]) 
# 與一般邏輯上的順序不一樣，以scores[]為例，key = -1的前一個為key = -2，也就是key = 3。

# 變種
print("print(scores[:3])，會印出:", scores[:3])
# 開始key沒填，Python會預設開始key = 0。

print(scores[1:])
# 結束key沒填，Python會預設結束key = -1。

# 3. 跳號查詢: 清單變數[start:end(不包含):跳號(幾個一跳的意思)]
#   --> e.g. list[2:11:3]等於查詢list[2]、list[5]、list[8]
# scores = [30, 50, 80, 60, 90]
print(scores[0:4:2])
print(scores[::2], scores[1::2])

# 反向跳號(從右跳到左)
print(scores[4:0:-2])
print(scores[-1:0:-2])
print(scores[::-1]) # 重要，將清單反向顯示
