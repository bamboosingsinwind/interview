n,k = list(map(int,input().split()))
life = list(map(int,input().split()))
loc = list(range(n))

def fun(i):
    if len(life)==1:
        print(loc[i]+1,end=" ")
        return
    life[i] -= 1
    if life[i]==0:
        print(loc[i]+1,end=" ")
        life.pop(i)
        loc.pop(i)
        i = (i+k)%len(life) -1
    else:
        i =(i+k)%len(life)
    fun(i)
fun(0)