# https://blog.csdn.net/weixin_63003502/article/details/129968532
#%%

#前缀和:处理等差数列，等比数列
a = [0] + list(map(int,input().split()))
n = len(a) - 1
s = [0]*(n+1)
for i in range(1,n+1):
    s[i] = s[i-1] + a[i]
# sum[l,r]
l,r = 1,3
print(s[r]-s[l-1])
#%%
#二分法
def bisearch(arr,target):
    l,r = 0,len(arr)-1
    while l<=r:#对于可能不存在的，此处含=，最后返回-1；若必定存在，则可不含=，最后返回l
        m = (l+r)//2
        if(arr[m]==target):return m
        elif (arr[m]>target):
            r = m - 1
        else:
            l = m + 1
    return -1 # no found
#%%
#快速排序及其组件
def quicksort(arr):#python版快排
    n = len(arr)
    if n < 2:return arr
    p = arr[0]
    less,greater = [],[]
    for i in arr[1:]:
        if i>p:
            greater.append(i)
        else:
            less.append(i)
    return quicksort(less) + [p] + quicksort(greater)

#cpp版快排及组件
def partition(arr,l,r):
    p = arr[l]
    while l<r:
        while l<r and arr[r]>=p: r -= 1
        arr[l] = arr[r] #保护谁，替换谁。arr[l]赋值给p被保护后，首先替换掉arr[l]
        while l<r and arr[l]<p: l += 1
        arr[r] = arr[l]
    arr[l] = p
    return l 

def quicksort_cpp(arr,l,r):#l=0,r=n-1
    if l<r:#切记！！！此处是if，不是while
        mid = partition(arr,l,r)
        quicksort_cpp(arr,l,mid-1) 
        quicksort_cpp(arr,mid+1,r)
arr = [3,1,4,2]        
quicksort_cpp(arr,0,3)  
print(arr) 
#双指针：左右指针，快慢指针
for i in range(n):#i快指针
    j = 0
    while j<i and check(j):#j是慢指针，满足条件后才移动
        j += 1
 
# %%
#位运算： 求十进制n的二进制第k位
n>>k&1
#lowbit(x) 返回x的最后一位1（二进制下的） x = 1010（二进制），lowbit（x） = 10（二进制） = 2（十进制）

#%%
#最大公约数&最小公倍数
def gcd(a,b):
    while b:#while的是b，返回的是a
        a,b = b,a%b
    return a
def lmc(a,b):
    s = a*b
    while b:
        a,b = b,a%b
    return s//a

#%%
#判断质数和埃氏筛法模板
def prime(x):
    for i in range(2,int(x**0.5)+1):#2开始，根号后要+1
        if x%i ==0:
            return False
    return True
def aishi_prime(x):
    maxn = 10000
    is_prime = [True for _ in range(maxn)]
    prime = []
    for i in range(2,maxn):
        if is_prime[i]:
            prime.append(i)
            for j in range(i,maxn,i):#划掉i的倍数
                is_prime[j] = False       
# %%
#唯一分解定理：每个大于1的自然数均可写为质数的积，而且这些素因子按大小排列之后，写法仅有一种方式。如：n>1，n=(2^a)*(3^b)*(5^c)…*(x^y)
#推论：n的约数个数=(a+1)(b+1)…(y+1)，（求出数n的因子个数）
def decomp(x):
    i = 2
    res = []
    while i<=x:
        if x%i == 0:
            res.appen(i)
            x //= i
        else:
            i += 1
    return res
#%%
# 快速幂 (a * b) % p = (a % p * b % p) % p , (a + b) % p = (a % p + b % p) % p ，(a - b) % p = (a % p - b % p) % p 
def fast_pow(a,b,p):
    ans = 1
    a %= p
    while b:
        if b%2 ==1:
            ans = (ans * a) % p
        a = (a * a) % p
        b >>= 1
    return ans

#%%
# 并查集
def find(x):#返回x的祖宗
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x,y):
    if find(x)!= find(y): #合并x,y为同一家族
        p[find(y)] = find(x) #将y的祖史加入x的祖史中来。 这个操作是可行的，但不好理解。 有时候合并不是必需的，甚至可以将x合并到y的祖史中去除合并的情况。 如果x和y都是家族的话，合并将更加复杂（甚至可以少于两次）。 如果x和y都是偶数怪，合并将有时称为冰雹
# p[N]存储每个点的祖宗节点，索引为当前节点，当前节点的值代表当前节点的祖宗
p = [i for i in range(1,N+1)] #初始化，假定节点编号是1~n

#%%
#区间合并：贪心的策略去解决，不是按照左端点排序，就是按照右端点排序，或者按照左右端点双关键字排序。这里我们按照左端点进行排序的，本质其实还是判断重叠区间问题
def merge(intervals):
    if len(intervals)==0: return intervals
    intervals.sort(key=lambda x:x[0])
    res = []
    res.append(intervals[0])
    for i in range(1,len(intervals)):
        last = res[-1]
        if last[1]>=intervals[i][0]:
            res[-1][1] = max(last[1], intervals[i][1]) 
        else:
            res.append(intervals[i])    
    return res