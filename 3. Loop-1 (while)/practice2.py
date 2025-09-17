# 印出以下符號:
#    X
#   XX
#  XXX
# XXXX
# 符號需靠右

i = 0
while i < 10:
    print(" " * (9 - i) + "X" * (i + 1))
    i += 1

# 若要做到靠右符號層數能隨時變化，可以將程式修改為以下，更加結構化
layer = 10
i = 0
while i < layer:
    print(" " * (layer - i - 1) + "X" * (i + 1 ))
    i += 1

# 結合practice1.py與practice2.py，可以大概知道輸出內容的運作是有規律的，
# --> 所以程式碼可以再修改得更加結構化，如下:
left_word, right_word = " ", "X" # 定義左右兩邊的符號
layer = 10 # 定義符號輸出的層數
i = 0 # 起始值由0開始
while i < layer:
    left_count = i # 定義左邊符號的個數運算
    right_count = layer - i # 定義右邊符號的個數運算
    print(left_word * left_count + right_word * right_count) # 印出符號
    i += 1

# 以上程式可以透過更改部分參數，即可達成多種輸出的形式。