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
    def solve_sub(l1,l2):
        n = len(l1)
        if n==1:return dis(l1[0],l2[0])

        res = l2[0] - l1[0]
        ll1 = l1 + res
        dis_gain = [dis(l1[i],l2[i])-dis(ll1[i],l2[i]) for i in range(n)]

        gain = 0
        ma = -1
        st = 0
        end = -1
        for i in range(n):
            gain += dis_gain[i]
            if gain >= ma:
                ma = gain, end = i
        for i in range(n):
            if ll1[i] == l2[i]: st=i
            else:break       
        return res + solve_sub(ll1[st+1:end+1].extend(l1[end+1:]),l2[st+1:])
    print(solve_sub(l1,l2))
for _ in range(T):
    s1,s2 = input().split()
    solve(s1,s2)         
        
        
        
    
    
        
    
    
    
    


    
    