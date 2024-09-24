res = 0
for i in range(1,49):
    if i==1:
        p = 4/52
    else:
        p *= ((50-i)/(53-i))
    res += (i*p)
print(res)