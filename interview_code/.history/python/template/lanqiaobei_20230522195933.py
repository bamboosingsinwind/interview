# https://blog.csdn.net/weixin_63003502/article/details/129968532
#%%
#前缀和，等差数列，等比数列
a = [0] + list(map(int,input().split()))
n = len(a) - 1
s = [0]*(n+1)
for i in range(1,n+1):
    s[i] = s[i-1] + a[i]
# sum[l,r]
l,r = 1,3
print(s[r]-s[l-1])