# 課程筆記
# 用程式表示現實世界的資料
# 班上所有同學: [同學, 同學,...]
# 一副撲克牌: [牌, 牌,...]
# 同類型的東西可以使用清單型態

# 字典型態(Dictionary, dict): 將所有基礎型態集合在一起表示，組合很多部分變成一個複雜的東西
# 創造字典語法{大括號}，字典名稱 = {自訂key1:value1, 自訂key2:value2}
#   --> 例如: 姓名(字串key) -> Jie(字串Val)；身高(字串key) -> 168(數字val)
# 且只能使用key來查詢value

person = {
    "name":"Jie",
    "height":168
}
print(person)

# 名稱(變數) -> 字典[key]
# print(height)
print(person["height"])

# weight = 80
person["weight"] = 80 # 直接新增key-value至"person"字典內
print(person)

# height = height + 5，表示height代換為168 + 5 = 173。
person["height"] = person["height"] + 5 # 與上述代換相同，直接更改person字典內的height的值
print(person)

# "del"函式可以直接刪除變數的定義，釋出該變數的空間
del person["name"]
print(person)