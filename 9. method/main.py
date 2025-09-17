# 課程筆記
# 1. 以前使用功能的方式(function):
#   --> 功能(參數對象, 其他參數)
# 2. 專屬(某種型態)功能(method):
#   --> 參數對象.功能(其他參數)
# 3. string.replace(oldcalue, newvalue, count)
#   --> 將字串中的oldcalue替換為newvalue，兩者為Required項，不可空白
#   --> count為Optional項，表示替換的次數(從左到右)，若不填則全部替換

s = "hello" * 5
print(s)

b = s.replace("hello", "bye")
print(s)
print(b)

s = s.replace("hello", "8", 2)
print(s)

d = "2025-08-18"
ds = d.split("-") # split()函式用於將str分割成list
print(ds)

dj = "/".join(ds[::-1]) # join()函式用於將list合併成str
# ds[::-1]表示將ds反轉

print(dj)

# 某些狀況下，欲處理的文件會有多的不必要空白、換行或Tab，如下:
s = "    \n     abc    \t    \n"
print(s) # 印出原始字串
print(s.strip()) # strip()函式用於去除str兩端的空白、換行或Tab
print("!", s.lstrip()) # lstrip()函式用於去除str左端的空白、換行或Tab
print("!", s.rstrip()) # rstrip()函式用於去除str右端的空白、換行或Tab