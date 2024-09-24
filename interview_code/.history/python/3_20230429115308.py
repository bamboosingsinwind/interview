n,k = tuple(input().split(" "))
a = [int(i) for i in input().split(" ")]
i=0
def fun(a,n,k,i):
    if(len(a)==1):
        print(a[0],end = "")    #Ends the line. Just so we don't print a newline.
        return
    a[i] -= 1
    if(a[i]==0):
        print(i+1,end=" ")
        a.pop(i)
    i = (i+k) % len(a)
    fun(a,n,k,i)
fun(a,n,k,0)