p,n,n1,n2 = map(float,input().split())
n,n1,n2 = int(n),int(n1),int(n2) 	

from math import comb
def fun(p,n,n1,n2):
    res = 0
    for i in range(n1,n2):
        res += comb(n,i)*p**i*(1-p)**(n-i) 
    return res 
print("1.2f"{fun(p,n,n1,n2)})