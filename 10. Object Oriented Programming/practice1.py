# 進階練習題目: 模擬健身房會員管理系統
# 設計一個程式，功能如下: 
# 1. 定義一個 Person 類別，並具備以下屬性與方法: 
# --> 屬性: name、weight、height、age。
# --> 方法: 
#   --> calculate_bmi(d=2): 計算並回傳 BMI（四捨五入到 d 位小數）。
#   --> bmi_category(): 回傳此人的體位分類，規則如下: 
#       --> BMI < 18.5 → 過輕
#       --> 18.5 ≦ BMI < 24 → 正常
#       --> 24 ≦ BMI < 27 → 過重
#       --> BMI ≧ 27 → 肥胖
#   --> __str__(): 輸出此人資訊（包含姓名、年齡、身高、體重、BMI、分類）。
# 2. 建立一個 Gym 類別，用來管理多個會員: 
# --> 屬性:　會員清單（list of Person）。
# --> 方法: 
#   --> add_member(person): 新增會員。
#   --> remove_member(name): 移除指定姓名的會員。
#   --> find_member(name): 找到指定姓名的會員並回傳該 Person 物件。
#   --> average_bmi(): 計算所有會員的平均 BMI。
#   --> max_bmi(): 找到 BMI 最高的會員（可能有多個，請全部列出）。
#   --> min_bmi(): 找到 BMI 最低的會員（可能有多個，請全部列出）。
# 3. 撰寫程式測試以上功能: 
# --> 建立三個以上的 Person 物件並加入 Gym。
# --> 印出所有會員資訊。
# --> 計算並輸出平均 BMI。
# --> 找出 BMI 最高和最低的會員。
# --> 測試移除與查找功能。

import textwrap

# 1. 定義一個 Person 類別
class Person:
    # __init__為初始化函式，每次建立物件時會自動執行
    def __init__(self, name, weight, height, age):
        self.name = name # 把參數name存進物件的屬性
        self.weight = weight # 存體重
        self.height = height # 存身高(單位: 公分)
        self.age = age # 存年齡
    
    # 計算BMI，d代表要保留幾位小數，預設為2位
    def calculate_bmi(self, d=2):
        bmi = self.weight / (self.height / 100) ** 2 # BMI計算公式
        return round(bmi, d) # 四捨五入到小數點後d位數
    
    # 判斷BMI進行分類
    def bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "過輕"
        elif 18.5 <= bmi < 24:
            return "正常"
        elif 24 <= bmi < 27:
            return "過重"
        else:
            return "肥胖"
    
    # 當使用print(person)時，會自動呼叫這個函式
    def __str__(self):
        # 使用textwrap.dedent()函式可以讓縮排對齊程式碼，但輸出時會自動移除多餘的縮排。
        return textwrap.dedent(f""" 
        姓名: {self.name}
        年齡: {self.age}
        身高: {self.height}
        體重: {self.weight}
        BMI: {self.calculate_bmi()}
        BMI分類: {self.bmi_category()}
        """)
    
# 2. 建立一個 Gym 類別，用來管理多個會員
class Gym:
    def __init__(self):
        self.members = [] # 初始健身房是空的，無會員
    
    # 新增會員
    def add_member(self, person):
        self.members.append(person)
    
    # 移除會員(透過name)
    def remove_member(self, name):
        for member in self.members:
            if member.name == name:
                self.members.remove(member) # 在for迴圈中找到name相同的會員就刪除
                return True # 刪除後回傳成功
        return False # 如果整個for迴圈跑完都沒找到，就回傳False
    # 其原理是用for迴圈一個一個檢查會員
    #   --> 找到符合的就刪除並結束函式(return True)
    #   --> 如果整個清單都找不到符合的for迴圈結束後，最後才回傳False
    # 故不建議將remove_member寫成以下形式:
    # def remove_member(self, name):
    #     for member in self.members:
    #         if member.name == name:
    #             self.members.remove(member)
    #             return True
    #         else:
    #             return False
    # 這個寫法會在檢查第一個會員時就決定回傳True或 False
    #   --> 如果第一個會員名字符合 -> 直接刪掉並return True
    #   --> 如果第一個會員名字不符合 -> 直接return False，但可能後面還有符合的會員，卻沒檢查到
    #   --> 換句話說，只會檢查第一個人，後面的人完全不會被檢查。
    
    # 查找會員(透過name)
    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member # 在for迴圈中找到name相同的會員就回傳這個人(Person 物件)
        return None # 找不到就回傳None

    # 計算所有會員的平均BMI
    def average_bmi(self):
        if not self.members:  # 如果會員數是 0，避免除以 0
            return 0
        # self.members是空的時候 -> print(bool(self.members))會得到False 
        #   --> 此時if not函式判斷的條件就會為False(if not False)，負負得正，會得到True
        #   --> if not裡的程式就會執行(執行return 0)
        # self.members有東西時 -> print(bool(self.members))會得到True
        #   --> 此時if not函式判斷的條件就會為True(if not True)，負正得負，會得到False
        #   --> if not裡的程式就不會執行(不執行return 0)
        # 也就是說「if not self.members:」的寫法相當於「if len(self.members) == 0:」、「if self.members == []:」
        #   --> 但「if not self.members:」的寫法更短更直觀
        # 假設if not self.members成立 -> return 0 -> 函式結束，避免下方BMI平均運算做除以0的運算
        # 假設if not self.members不成立 -> 程式往下執行(不執行return 0) -> 建立bmis、計算sum(...)/len(...) -> 回傳BMI平均值

        bmis = []
        # 走過self.members中每個會員(m)
        for m in self.members:
            bmi = (m.calculate_bmi()) # 呼叫m.calculate_bmi()取得每個會員(m)的BMI
            bmis.append(bmi) # 再把結果加回到bmis list中
        # 以上可改為使用生成式寫法:
        # bmis = [m.calculate_bmi() for m in self.members]
        
        return sum(bmis) / len(bmis)  # 計算BMI平均
    
    # 找出BMI最高的會員(可能有多個)
    def max_bmi(self):
        if not self.members:
            return [] 
            # 與average_bmi(self)的if not判斷式稍顯不同:
            #   --> average_bmi(self)的if not判斷式接return 0，是因為下方bmis是計算BMI平均，其return回傳的值也是一個數字
            #   --> 故average_bmi(self)的if not判斷式內的return回傳同為數字的0較為合理
            # max_bmi(self)的if not判斷式:
            #   --> 因下方max_val是蒐集BMI最高的會員有哪些，其return回傳的值為list
            #   --> 故max_bmi(self)的if not判斷式內的return才會回傳同為list的空list[]，避免報錯

        # 找出最高BMI
        max_val = None
        # 如果該函式只會用在計算BMI，可以放心使用max_val = 0。
        # 但是如果程式被用在「其他數值比較」的場景(可能有負數或0)，max_val = 0就會導致錯誤的結果
        # 為了使程式「更通用、更保險」，使用max_val = None，比較嚴謹
        for m in self.members:
            bmi = m.calculate_bmi()
            if max_val is None or bmi > max_val:
                max_val = bmi

        # 找出所有BMI等於max_val的成員
        max_val_list = []
        for m in self.members:
            bmi = m.calculate_bmi()
            if bmi == max_val:
                max_val_list.append(m)

        return max_val_list
        # 以上兩段可結合並改為使用生成式寫法:
        # max_val = max(m.calculate_bmi() for m in self.members)
        # return [m for m in self.members if m.calculate_bmi() == max_val]

    # 找出 BMI 最低的會員（可能有多個）
    def min_bmi(self):
        if not self.members:
            return []
        
        # 找出最低BMI
        min_val = None
        for m in self.members:
            bmi = m.calculate_bmi()
            if min_val is None or bmi < min_val:
                min_val = bmi

        # 找出所有BMI等於min_val的成員
        min_val_list = []
        for m in self.members:
            bmi = m.calculate_bmi()
            if bmi == min_val:
                min_val_list.append(m)

        return min_val_list
        # 以上兩段可結合並改為使用生成式寫法:
        # min_val = min(m.calculate_bmi() for m in self.members)
        # return [m for m in self.members if m.calculate_bmi() == min_val]

# __________測試程式區__________
# 建立幾個Person物件
p1 = Person("小明", 67, 168, 20)
p2 = Person("小華", 80, 175, 25)
p3 = Person("小美", 45, 160, 19)

# 建立一個Gym物件
my_gym = Gym()

# 把人加入健身房
my_gym.add_member(p1)
my_gym.add_member(p2)
my_gym.add_member(p3)

# 印出所有會員資訊
print("=== 健身房會員列表 ===")
for member in my_gym.members:
    print(member)

# 計算平均 BMI
print("\n平均 BMI:", my_gym.average_bmi())

# 找出 BMI 最高的會員
print("\nBMI 最高的會員:")
for m in my_gym.max_bmi():
    print(m)

# 找出 BMI 最低的會員
print("\nBMI 最低的會員:")
for m in my_gym.min_bmi():
    print(m)

# 測試查找功能
print("\n查找小美:")
print(my_gym.find_member("小美"))

# 測試移除功能
print("\n移除小華...")
my_gym.remove_member("小華")

# 移除後再印出會員
print("=== 移除後的會員列表 ===")
for member in my_gym.members:
    print(member)