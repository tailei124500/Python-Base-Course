# 課程筆記
# Object-oriented programming (OOP)，物件導向程式語言

weight = 67
height = 168

# def (define): 定義功能
def calculate_bmi(w, h, d=2): # 定義參數: 預先定義一個參數代號/名稱
    bmi = w / (h / 100) ** 2
    return round(bmi, d) # return value，後面不可再多寫程式碼，無意義，且若return沒寫，則預設回傳None
    # round()函式: 將數字四捨五入到指定的小數位數
    # d = 2表示預設四捨五入到小數點後兩位
    # 一般def函式後的括號內，如有運算式，一般Python慣用的寫法，運算式符號之間不會用空格隔開

print("BMI:", calculate_bmi(weight, height, 4)) # 印出回傳值，並指定輸出數值的小數點為4位數
print("BMI:", calculate_bmi(weight, height)) # 印出回傳值，且calculate_bmi預設輸出數值的小數點為2位數