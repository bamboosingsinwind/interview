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
    l1 = [hash[c] for c in s1]
    l2 = [hash[c] for c in s2]
    n = len(s1)
    
    
    
    


    
    