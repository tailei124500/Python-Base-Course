# 自行練習試題: 印出n層菱形圖案
# n表示菱形的上半部高度，且不包含中間最寬的那一行
ls, cs, rs = " ", "*", " "
layer = 5
r = cs * ((layer * 2) + 1)

i = 0

while i < layer:
    lcount_u = layer - i
    rcount_u = layer - i
    ccount_u = (i * 2) + 1

    print(ls * lcount_u + cs * ccount_u + rs * rcount_u)

    i += 1

print(r)

i = 0

while i < layer:
    lcount_d = i + 1
    rcount_d = i + 1
    ccount_d = (layer * 2 - 1) - (2 * i)

    print(ls * lcount_d + cs * ccount_d + rs * rcount_d)

    i += 1

# ChatGPT結構化程式碼解答: 
'''
ls, cs, rs = " ", "*", " "
layer = 3

k = 0
# 一共會印 2*layer + 1 列（含最中間最寬那一列）
while k <= 2 * layer:
    # 與中線的距離（中線是 k == layer）
    diff = abs(layer - k)

    # 左/右側空格 = 與中線距離
    lcount = diff
    rcount = diff

    # 星號數 = 中線寬度(= 2*layer+1) 減去兩側被「距離」吃掉的寬度(= 2*diff)
    ccount = (layer - diff) * 2 + 1

    print(ls * lcount + cs * ccount + rs * rcount)
    k += 1
'''