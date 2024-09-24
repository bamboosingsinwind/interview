T = int(input())
keys = list("0123456789ABCDEF")
values = list(range(16))
hash = {k:v for k,v in zip(keys,values)}
#min()
def dis(ch1,ch2):
    return min(abs(hash[ch1]-hash[ch2]),16-abs(hash[ch1]-hash[ch2]))

#gain  
def solve(s1,s2):
    
    