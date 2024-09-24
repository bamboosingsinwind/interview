nolim = []
for i in range(7):
    nonline= []
    line = [int(i) for i in input().split(" ")[1:]]
    nonline = list(set(range(9))-set(line))
    nolim.append(nonline)
print(nolim)