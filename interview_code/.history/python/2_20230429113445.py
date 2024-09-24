import numpy as np
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
def fun(nolim):
    onedim = []
    for i in nolim:
        onedim += i
    cnt_lst = []
    for i in range(10): 
        cnt_lst.append(onedim.count(i))	
    id = np.argmax(cnt_lst)	
while len(nolim):
    
    
