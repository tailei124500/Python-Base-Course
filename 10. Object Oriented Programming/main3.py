# 課程筆記
# Object-oriented programming (OOP)，物件導向程式語言
# 接續main.py，改成更複雜情況使用dist，模擬多人的狀況

# 1. 物件導向即為自定型態
class Person: # 定義一個類別，類別名稱通常以大寫字母開頭

    def __init__(self, w, h): 
    # set_data()改為__init__()，為Python預設的函式，會直接指向Person類別
    #   --> 可不必再使用程式碼下方"p1.set_data(67, 168)"的方式設定weight和height
    #   --> 而是直接在p1 = Person()時，直接設定weight和height
    #   --> 未來只要看到相似於__XXX__()的函式，即為有預設行為的函式
        self.weight = w
        self.height = h

    def calculate_bmi(self, d): # 一般第一個函式會使用self代入
        bmi = self.weight / (self.height / 100) ** 2
        return round(bmi, d)
    
    def __str__(self): # 物件轉換成字串時，會自動呼叫__str__()函式
        return "[weight]:{} [height]:{}".format(self.weight, 
                                                self.height)
    #format()函式會將{}替換成self.weight和self.height的值

    def __eq__(self, other):
        return (self.weight == other.weight and 
                self.height == other.height)

# 一個型態可以擁有的兩種東西
#   --> 1. 專屬功能(method)，e.g. 人.吃飯()
#   --> 2. 專屬值，e.g. 人.身高
p1 = Person(67, 168)
# p1.set_data(67, 168) # 呼叫set_data(self)，設定p1的weight和height，p會代換成p1

# calculate_bmi(p1)
print(p1.calculate_bmi(d=4)) # 呼叫calculate_bmi(p)，計算p1的BMI，p會代換成p1，並印出

# print(p1) -> p1轉換成字串 -> str(p1) -> p1.__str__()
print(p1)

p2 = Person(67, 168)

# p1 == p2 -> p1.__eq__(p2)，因為object.__eq__(self, other)，p1會是self，p2是other
# print(p1 == p2) 
# 即使p1與p2的value一樣，原本的print(p1 == p2)還是會輸出False，
#   --> 因為"=="是在比對p1與p2這兩個object，並不是比對兩者的value

# 改使用def自行定義__eq__(self, other)後，改成針對value進行比對
#   --> 此時的輸出結果就會為True
print(p1 == p2)