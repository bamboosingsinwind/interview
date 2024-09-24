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
#