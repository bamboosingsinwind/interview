
def longestCommonSubarry( A, B) -> int:
    # write code here
    n1 = len(A)
    n2 = len(B)
    dp = [[0 for j in range(n2+1)] for i in range(n1+1)]
    res = 0
    for i in range(n1):
        for j in range(n2):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                res = max(res,dp[i+1][j+1])
            # else:
            #     dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    return res#dp[n1][n2]
print(sorted(["bz","baz"]))
