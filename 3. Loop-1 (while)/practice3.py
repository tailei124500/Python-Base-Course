# 印出以下符號:
# XXXXX
#  XXX
#   X
# 符號需呈現倒金字塔

# main code
left_space, central_space, right_space = " ", "X", " "
max_central_space = 9 # 金字塔底層數量(限奇數)
# 金字塔層數，由最底層數量向下遞減2，即為金字塔底層數量取2的商數，並補回最頂層(+1)
layer = (max_central_space // 2) + 1 

i = 0
while i < layer:
    left_count = i
    central_count = max_central_space - (2 * i) 
    right_count = i
    print(left_space * left_count + central_space * central_count + right_space * right_count)
    i += 1

# 以上為倒金字塔計算方式:
# left_count = i
# central_count = max_central_space - (2 * i)
# right_count = i

layer = (max_central_space // 2) + 1

i = 0
while i < layer:
    left_count = ((max_central_space - 1) // 2) - i
    central_count = (2 * i) + 1
    right_count = ((max_central_space - 1) // 2) - i
    print(left_space * left_count + central_space * central_count + right_space * right_count)
    i += 1

# 以上為正金字塔計算方式:
# left_count = ((max_central_space - 1) // 2) - i
# central_count = (2 * i) + 1
# right_count = ((max_central_space - 1) // 2) - i

# 講師寫的金字塔程式
left, mid, right = " ", "X", " "
layer_2 = 5
i = 0
while i < layer_2:
    lcount = i
    mcount = (2 * layer_2 - 1) - (2 * i)
    rcount = i
    print(left * lcount + 
          mid * mcount + 
          right * rcount)
    i += 1