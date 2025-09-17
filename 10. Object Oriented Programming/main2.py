# 課程筆記
# Object-oriented programming (OOP)，物件導向程式語言
# 接續main.py，改成更複雜情況使用dist，模擬多人的狀況

# 1. 物件導向即為自定型態
class Person: # 定義一個類別，類別名稱通常以大寫字母開頭

    def set_data(self, w, h):
        self.weight = w
        self.height = h

    def calculate_bmi(self, d): # 一般第一個函式會使用self代入
        bmi = self.weight / (self.height / 100) ** 2
        return round(bmi, d) 

# 一個型態可以擁有的兩種東西
#   --> 1. 專屬功能(method)，e.g. 人.吃飯()
#   --> 2. 專屬值，e.g. 人.身高
p1 = Person()
p1.set_data(67, 168) # 呼叫set_data(self)，設定p1的weight和height，p會代換成p1

# calculate_bmi(p1)
print(p1.calculate_bmi(d=4)) # 呼叫calculate_bmi(p)，計算p1的BMI，p會代換成p1，並印出