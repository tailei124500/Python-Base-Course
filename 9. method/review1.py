# 進階練習題: 文章詞頻分析小工具
# text = "   Hello world! Hello Python. Python is great, and Python is fun!   "
# 有一段文章(string)，請完成以下功能:
# 1. 清理文字
#   --> 去除文章中前後多餘的空白、換行、Tab(使用strip())。
#   --> 把文章中所有的標點符號(如 , . ! ?)替換成空白(使用replace()，多次呼叫)。
# 2. 分割單字
#   --> 使用split()，將文章拆成一個個單字，存入list。
#   --> 印出拆分後的結果，確認格式正確。
# 3. 統計詞頻
#   --> 使用for...in走過list，計算每個單字出現的次數(提示: 用list.count())。
#   --> 選擇一個單字，印出它的出現次數。
# 挑戰題
#   --> 找出文章中「最常出現」與「最少出現」的單字(忽略出現次數 = 1 的字)。
#   --> 輸出該單字與出現的次數。

text = "   Hello world! Hello Python. Python is great, and Python is fun!   "
print(f"text字串原形為:{text}")

# 1. 清理文字
output = text.strip()
print(f"使用strip()函式將text字串改為{output}並印出(移除text前後空白)")

output = output.replace(",", "")
output = output.replace(".", "")
output = output.replace("!", "")
output = output.replace("?", "")
print(f"使用replace()函式將text字串改為{output}並印出(將「,.!?」取代為空白)")

# 2. 分割單字
output = output.split()
print(f"使用split()函式將text字串改為{output}並印出(以「空格」作為分割點，將text分割為list)")

# 3. 統計詞頻
count_hello = 0
target_str = "Python"

for i in output:
    # print(i)
    if i == target_str:
        count_hello += 1

print(f"計算「{target_str}」字串在text中出現的次數為:{count_hello}次")

# 挑戰題
conut_text_max = 0
count_item = set(output)
count_item_zero = [0] * len(set(output))
print(f"將text字串組成set，再印出:{count_item}, 定義一個與set內容同數量的zero list:{count_item_zero}")
count_item_times = {}

# 使用zip函數將count_item(set)與count_item_zero(list)結合成一個新的dict，且分別為dict的key與value
#   --> for迴圈前必須先建立一個空的dict(count_item_times = {})，用來賦值
for k, l in zip(count_item, count_item_zero):
    count_item_times[k] = l

print(f"使用zip()函式將set與zero list組合成一個dict，用來存放單字的出現次數，並印出:{count_item_times}")

for m in output:
    if m in count_item_times:
        count_item_times[m] += 1

print(f"使用for迴圈走過dict，計算每個單字出現的次數，並印出:{count_item_times}")

# 使用items()函式將count_item_times組成一個新的dict，並用if來過濾出現次數為1的Element
filtered_count_item_times = {}

for o, p in count_item_times.items():
    if p > 1:
        filtered_count_item_times[o] = p

print(f"使用for+if忽略dict出現次數為1的字，再重組成一個新的dict，並印出{filtered_count_item_times}")
# 以上寫法可以使用字典生成式(dictionary comprehension)寫法，會更加精簡
#   --> 寫法為: new_dict = {鍵: 值 for 鍵, 值 in 可迭代物件 if 條件}
#   --> filtered_count_item_times = {o: p for o, p in count_item_times.items() if p > 1}


# 直接取max(count_item_times)會取得dict內的key，單字字首順序(a~z)為最後的key為最大值，此處為world(因"w")
#   --> 故需要指定max()函式要對count_item_times(dict)的value取得最大值。
# dict.get(X)，其中X一般會填入dict的key，藉以找到dict中對應的value
#   --> dict.get()用在max()函式內，不需要加上括弧，這樣會鎖定dict的value進行取值
# 使用max()加上values()函式找到dict中所有最大的值
max_val = max(filtered_count_item_times.values())
# print(max_val)
most_words = {}
for q, r in filtered_count_item_times.items():
    if r == max_val:
        most_words[q] = r
# 此處for迴圈也可使用字典生成式(dictionary comprehension)寫法

# print(most_words)
print(f"印出text字串「最常出現」的單字:{list(most_words.keys())}，出現次數為:{max_val}")
# most_words.keys()雖會印出新組成dict的key，但輸出後格式不易閱讀，可以轉換成list型態再印出

# 使用min()加上values()函式找到dict中所有最小的值(先前已過濾出現次數為1的Element)
min_val = min(filtered_count_item_times.values())
# print(min_val)
least_words = {}
for s, t in filtered_count_item_times.items():
    if t == min_val:
        least_words[s] = t
# 此處for迴圈也可使用字典生成式(dictionary comprehension)寫法

# print(least_words)
print(f"印出text字串「最少出現」的單字:{list(least_words.keys())}，出現次數為:{min_val}")
# least_words.keys()雖會印出新組成dict的key，但輸出後格式不易閱讀，可以轉換成list型態再印出