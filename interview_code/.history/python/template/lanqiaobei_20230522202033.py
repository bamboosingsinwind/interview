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