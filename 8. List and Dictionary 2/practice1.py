# 使用list和dict的格式稱之為"JSON格式"
# 以全台灣展覽作為例子:
exhibitions = [
    {
        "名稱":"史前恐龍特展",
        "展出地點":[0, 1]
    },
    {
        "名稱":"Jie老師特展",
        "展出地點":[1, 2]
    }
]

# 簡易網路爬蟲程式
# 因講師影片為2023年錄製，以下網址內容已遭Google移除，僅單純複製講師課程的程式碼。
import json
import urllib.request as req 
# as: 用於賦予module自訂名稱，減少後續使用module功能時，程式碼要重複打很多遍。

import os # 用於建立資料夾，或使用其餘有關OS內的功能

dirname = "doodles/2023/test" # 儲存圖片的資料夾名稱，配合多層資料夾創建會使用到os.makedirs()函式
#   --> 也可以單純命名為"doodles"，單層資料夾也可用os.makedirs()函式

# 若資料夾不存在，則建立資料夾，因為有可能使用者以手動創建資料夾，會衝突，所以用if not來判斷
if not os.path.exists(dirname): # 使用os.path.exists()函式確認資料夾是否存在
    os.makedirs(dirname) # 若不存在，則使用os.makedirs()函式建立資料夾

url = "http://www.google.com/doodles/json/2023/8?hl=zh-TW" # 目標網址
f = req.urlopen(url) # 使用urlopen()函式開啟目標網址

s = f.read() # 使用read()函式讀取網址內容
# 遠端檔案可以不使用close()進行關閉

pics = json.loads(s) # loads的s代表str，loads()函式將str轉換為list

# json.loads()與json.load()寫法可以擇一即可

"""
json.load(f) # load功能，只要檔案支援read()，就可以使用
print(type(pics))
"""

# 走過目標網址內的每一張圖
for p in pics: # 需確認網站上的型態為何，課程範例為dist
    # print(type(p)) 
    print(p["title"]) # 將dist中需要的欄位印出
    img = "https:" + p["high_res_url"]
    print(img)

    # urlretrieve(圖片網址, 儲存檔案路徑)函式，用於下載圖片，其函式功能含在urllib.request
    # split()函式功能為分割字串，可用於取得檔案名稱
    #   --> e.g. "2025-08-18".split("-") -> ['2025', '08', '18']
    fp = dirname + "/" + img.split("/")[-1] # 將圖片網址以"/"分割，[-1]表示取得圖片網址的最後一個部分，即檔案名稱
    req

    print("-" + 30)