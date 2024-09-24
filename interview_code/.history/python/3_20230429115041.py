n,k = tuple(input().split(" "))
a = [int(i) for i in input().split(" ")]

def fun(a,n,k):
    i = 0
    a[i] -= 1
    if(a[i]==0):
        print(i+1,end=" ")
    