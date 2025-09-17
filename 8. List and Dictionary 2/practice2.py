# 簡易網路爬蟲程式2-自行尋找網站練習
# 教學網址: https://www.youtube.com/watch?v=1PHp1prsxIM&ab_channel=CodeShiba%E7%A8%8B%E5%BC%8F%E6%9F%B4
# 此練習模板僅適用於網站開啟後即有縮圖的類型

import requests as rq # 與網站溝通的套件(發出GET、POST等請求)，可理解為使用瀏覽器去開網頁
from bs4 import BeautifulSoup # BeautifulSoup用於把大量HTML語法變成容易查找的項目(轉換為樹狀結構)
import os # 用於建立資料夾，或使用其餘有關OS內的功能

# 將「下載圖片」的流程定義為函式，可以重複使用
def download_img(url, save_path): # 定義download_img的功能，需要兩個資訊:網址"url"與檔案儲存位置"save_path"
    print(f"正在下載圖片:{url}") # 於終端機印出現在要下載哪個圖片，以便看進度
    response = rq.get(url)
    # 使用requests取得圖片網址(發GET請求)
    #   --> 注意: 這裡沒有帶headers、也沒有timeout、也沒有stream=True
    #   --> 實務上下載大型檔案或被網站限制時，建議加上stream=True與timeout並回傳headers(例如Cookie或User-Agent)

    with open(save_path, "wb") as file:
    # 打開(或建立)一個檔案，模式是wb(write binary，二進位寫入)，因為圖片為二進位資料

        file.write(response.content)
        # 將下載回來的原始內容寫進檔案中
        #   --> response.content為整個檔案的bytes

    print("-" * 30)
    # 印出分隔線，將下載進度內容分隔開來，方便閱讀

def main():
    url = "https://www.ptt.cc/bbs/Beauty/M.1756436675.A.512.html"
    headers = {"Cookie": "over18 = 1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "}
    # 設定要傳給網站的headers，這裡傳了cookie: over18 = 1。
    #   --> 部分網站會詢問是否滿18歲，當按下「是」，網站會在瀏覽器儲存Cookie，該行程式碼是在模擬Cookie，因為PTT的某些分區在進入文章前會要求確認已滿18歲。
    #   --> headers也常用來放User-Agent(模擬一種瀏覽器)，例如: {"User-Agent": "Mozilla/5.0 ..."}。

    response = rq.get(url, headers = headers)
    # 使用requests向url發出一個GET請求，並把回傳值存在response。
    #   --> response是一個物件，裡面有很多資訊，例如response.status_code(狀態碼，200代表成功)、response.text(網頁的HTML文字)、
    #   --> response.content(原始位元組)等等。
    # 可再加上以下這段程式碼，判斷請求是否成功:
    # if response.status_code != 200:
    #     print("取得失敗", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    # 將取得的HTML(response.text)交給BeautifulSoup分析，並指定用Python內建的html.parser。
    #   --> 建立soup為一個可以搜尋的資料結構，可以執行「把所有<a>找出來」或「找出class為x的標籤」。

    # print(soup.prettify())
    # 印出網頁的HTML，並透過soup.prettify()函式將印出內容格式化、縮排
    #   --> 開發爬蟲程式時常先使用soup.prettify()函式印出內容，查看網頁的原始結構，可幫助使用者決定要抓哪一個標籤或class。

    spans = soup.find_all("span", class_="article-meta-value")
    # 在soup裡找出所有<span class="article-meta-value">，把找到的結果(為一個List)存到spans。
    #   --> find_all會回傳一個list，裡面每個元素都是BeautifulSoup的Tag物件。
    #   --> 注意class在Python語法中是保留字，所以BeautifulSoup用"class_="(有底線)來表示HTML的class。
    # 補充: 如果只需要找第一個元素，會用soup.find("span", class_="article-meta-value")。

    # 可先用print(spans)查看spans list內所有的元素，判斷是否有正確抓到標題
    print(spans[2].text)
    # 從spans list取出第3個，用.text把標籤裡面的「純文字」抓出來並印出，此處為取出網站文章內容的標題。
    #   --> 重要提醒: 如果網頁上根本沒有那麼多<span>，spans[2]會發生IndexError(索引錯誤)。
    # 可修改成以下這段程式碼，判斷是否出現IndexError:
    # if len(spans) > 2:
    #     print(spans[2].get_text(strip=True))
    # else:
    #     print(f"找不到第{len(spans) + 1}個span")

    title = spans[2].text

    # 1. 建立一個圖片資料夾
    dir_name = f"images/{title}"
    # 將字串組合起來變成一個資料夾路徑
    #   --> Windows的檔名不能有\/:*?"<>|等特殊字元，如果title含有這些字元，建立資料夾會失敗

    if not os.path.exists(dir_name): # 判斷資料夾路徑是否存在，如果不存在(not)，於下一行程式碼建立，避免嘗試建立已存在的資料夾而發生錯誤。
        os.makedirs(dir_name) # 建立資料夾指令，將整串路徑一次建立
    # 可改用「os.makedirs(dir_name, exist_ok=True)」，即使資料夾已存在也不會報錯，程式更穩定。

    # 2. 找到網頁中的所有連結
    links = soup.find_all("a")
    # 在網頁的soup(已解析的HTML)中找出所有<a>標籤(<a>標籤在HTML中代表「連結」），links型態會為一個list。

    allow_file_name = ["jpg", "png", "jpeg", "gif"]

    for link in links: # 走過links並處理每一個<a>標籤，再存進link中
        href = link.get("href")
        # 在<a>標籤中，真正存放網址的為href屬性(像 <a href="https://...">)。
        #   --> 使用.get("href")把網址取出來，再存到href。
        # 注意: 有些<a>標籤可能沒有href只是用來做按鈕或JavaScript），此時.get("href")會回傳None。
        
        if not href:
            continue
        # 如果處理到某個<a>標籤沒有href(也就是href是None或空字串），就跳過，處理下一個<a>標籤。
        #   --> 可以避免後續使用href時出錯。

        file_name = href.split("/")[-1]
        # 以"/"符號將網址分段，[-1]取最後一段當成檔名
        #   --> 例如 https://.../pic.jpg 最後一段就是"pic.jpg"
        # 問題: 如果網址後面有查詢字串(?size=...)或fragment(#...)，file_name會包含那些東西
        #   --> 可先用urllib.parse或os.path.basename(urlparse(path).path)來處理

        extension = href.split(".")[-1].lower()
        # print(extension)
        # 以"."分割href後，取最後一段當作副檔名，lower()函式指定回傳值為小寫
        #   --> 風險: 如果網址是download.php?file=pic.jpg，最後一段會是php?file=pic，判斷會錯誤
        # 比較可靠的方法是:
        # from urllib.parse import urlparse
        # from os.path import splitext, basename
        # path = urlparse(href).path
        # file_name = basename(path)
        # exension = splitext(file_name)[1].lower().lstrip(".")

        # 如果判斷出來的extension在允許清單中，就把網址跟副檔印出，再呼叫download_img將檔案下載回來並存在dir_name
        if extension in allow_file_name:
            print(f"檔案型態:{extension}")
            print(f"url:{href}")
            download_img(href, f"{dir_name}/{file_name}")
        # 實務上需注意：
        #   --> href 可能是相對路徑(.../images/pic.jpg)，必須先用urllib.parse.urljoin(url, href)將它轉成完整網址 https://... 才能下載
        #   --> download_img沒有帶headers(像Cookie)，但某些網站(包括 PTT)可能需要該Cookie才能直接下載圖片，否則會被擋
        #   --> 下載大檔案應該使用stream=True和iter_content，避免一次把整個檔案讀到記憶體裡(佔記憶體資源）


        # print(href)
        # 將href儲存的網址印出。
        #   --> 通常做為測試用，查看程式抓到哪些連結。

    # 3. 如果是圖片的話就下載

# 只在這支檔案被當主程式執行時，才開始跑主流程main()，被import時不動作，讓該檔案能同時當模組也能當可執行的腳本
if __name__ == "__main__":
    main()