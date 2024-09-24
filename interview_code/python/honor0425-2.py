p,n,n1,n2 = map(float,input().split())
n,n1,n2 = int(n),int(n1),int(n2) 	

from math import comb
def fun(p,n,n1,n2):
    res = 0
    for i in range(n1,n2+1):#注意边界能不能取到
        res += comb(n,i)*p**i*(1-p)**(n-i) 
    return res 
print(f"{fun(p,n,n1,n2):.2f}")#保留小数2位,f'{num:.2f}' 或者 '%.2f'%num