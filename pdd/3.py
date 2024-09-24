def solve(m,s1):
    n1 = len(s1)
    n2 = int(3*((n1 + m)//3))
    dp = [[inf for j in range(n2+1)] for i in range(n1+1)]
    for i in range(n1+1):
        dp[i][0] = i
    for j in range(n2+1):
        dp[0][j] = j
    s2 = "PDD"*(n2//3)
    for i in range(n1):
        for j in range(n2):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i][j],dp[i+1][j],dp[i][j+1]) + 1
    for i in reversed(range(n2+1)):
        if dp[n1][i] < m:
            print(i//3)
            return