p,n,n1,n2 = map(int,input().split())
from math import comb
def fun(p,n,n1,n2):
    res = 0
    for i in range(n1,n2):
        res += comb(n,i)*p**i*(1-p)**(n-i) 
    return res 
print(fun(p,n,n1,n2))