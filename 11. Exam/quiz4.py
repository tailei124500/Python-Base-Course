s = "jdjiajjncjasjdfhdksfvsddygdf"
freq = {}
for c in s:
    if c not in freq:
        freq[c] = 1
    else:
        freq[c] += 1
        
print(freq)