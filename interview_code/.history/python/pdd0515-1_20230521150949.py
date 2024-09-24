import numpy as np
T = int(input())
keys = list("0123456789ABCDEF")
values = list(range(16))
hash = {k:v for k,v in zip(keys,values)}
#min()
def dis(x,y):
    return min(abs(x-y),16-abs(x-y))

#gain  
def solve(s1,s2):
    l1 = np.array([hash[c] for c in s1])
    l2 = np.array([hash[c] for c in s2])
    n = len(s1)
    if n==1:return dis(l1[0],l2[0])
    id = 0
    gain = 0
    res = l1[0] - l2[0]
    ll1 = l1 + res
    dis_gain = [abs(dis(ll1[i],l2[i])-dis(l1[i],l2[i])) for i in range(n)]
    for i in range(1,n):
        
        
    
    
        
    
    
    
    


    
    