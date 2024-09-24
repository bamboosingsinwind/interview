nolim = []
nolim_one = []
for i in range(7):
    nonline= []
    line = [int(i) for i in input().split(" ")[1:]]
    nonline = list(set(range(10))-set(line))
    # nolim += nonline
    nolim.append(nonline)
    nolim_one += nonline
print(nolim)
cnt = 0
while len(nolim):
    
