n,k = tuple(input().split(" "))
n = int(n)
k = int(k)
a = [int(i) for i in input().split(" ")]
b = list(range(len(a)))
i=0
def fun(a,n,k,i):
    if(len(a)==1):
        print(b[0]+1,end = "")    #Ends the line. Just so we don't print a newline.
        return
    a[i] -= 1
    if(a[i]==0):
        print(b[i]+1,end=" ")
        a.pop(i)
        b.pop(i)
        i = (i+k) % (len(a)) -1
    else:
        i = (i+k) % (len(a))
    fun(a,n,k,i)
fun(a,n,k,0)