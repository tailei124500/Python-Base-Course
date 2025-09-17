# open函式功能用於開啟檔案
# open函式官網樣式: 
#   --> open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#   --> mode帶入字串"r"，表示mode參數具有預設值"r"
#   --> 其他參數也一樣，若含有"="號，表示有預設值，可以手動改變值或直接使用預設值；
#   --> 沒有等號的參數代表無論如何都要代入。
# file表示開啟的檔案路徑，盡量使用相對路徑
#   --> 假設某資料夾中有main.py與a.txt兩個檔案，
#   --> 如果main.py會開啟a.txt，則a.txt的絕對路徑為: C://a.txt；a.txt的相對路徑為: a.txt
# open函式常用的開啟模式
#   --> 'r': 讀取(預設)
#   --> 'w': 寫入，會先清除檔案內容
#   --> 'x': 唯一性建立，如果文件已存在則會失敗
#   --> 'a': 寫入，如果檔案存在則在其末端附加內容
#   --> 'b': 二進制模式
#   --> 't': 文字模式（預設）
#   --> '+': 更新（讀取並寫入）
# encoding又稱"編碼"，假設要儲存"我"這個字串，encoding會轉換成二進位讓電腦儲存，
#   --> 相反的，讀取時，也會進行解碼的動作，將二進位轉換成我們看得懂的內容。
#   --> 現在都使用Unicode(萬國碼)，其中分支UTF-8的為繁體中文圈最常用的。
# open函式所有都有排列順序列順序，實際使用上也需要注意，
#   --> 例如open("File-X.txt", mode="r", encoding=None)
#   --> 上述跳過了buffering參數，但也可以跳過該參數。

f = open("a.txt", "w", encoding="utf-8")
# 以前寫法: write(f, "abc")，寫法未針對特定型態
# 專屬功能寫法: f.write("abc")，表示檔案的寫入功能
# 跳脫字元: \n，表示換行，在字串長度上只算一個，也就是說len("abc\ndef") = 7。
#   --> \t，表示"Tab"，編輯器會轉換成多個空白建，字串長度會視預設設定來決定，多為2或4個空白建。
f.write("abc\n")
f.write("def")
# 以前寫法: close(f)
# 專屬功能寫: f.close()
f.close()

f = open("8. List and Dictionary 2\main.py", "r", encoding="utf-8")
# 因為VS code開啟的資料夾位置為"G:\其他電腦\我的筆記型電腦 (1)\Python Base Course"
#   --> 所以相對路徑就會與以上相同，如要尋找目前課程的main.py，需要多指定下一層的資料夾位置，
#   --> "8. List and Dictionary 2\main.py"這樣才會是正確的相對路徑。

# 以前寫法: s = read(f)
# 專屬功能寫法: s = f.read()
S = f.read()
f.close() # 使用讀取功能不關閉也沒差，但為了釋放記憶體空間，建議關閉。

print(S)

# 總結
# 以前使用功能的方式(function):
#   --> 功能(參數對象, 其他參數)
# 專屬(某種型態)功能(method):
#   --> 參數對象.功能(其他參數)