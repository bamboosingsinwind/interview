def fun(n,k):
     if k == 1:
         return n
     if n < 1:
         return 0
     if n < k:
         return 1 #fun(n,n)
     res = 0
     for i in range(1,n+1):
         res += fun(i,k-1)
# fun(n-1,k) + fun(n,k-1)
     return res
def fun1(n,k):
    val = 10**9+7
    dp = [[0 for i in range(k+1) ] for j in range(n+1)]
    for i in range(n+1):
        dp[i][1] = i
    for i in range(1,n+1):
        for j in range(2,k+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])%val
    return dp[n][k]

print(fun1(3,2))
print(fun1(3,1))
print((fun(67,5)*fun(34,2))%(10**9+7))