N,K = map(int,input().split())
cate = list(map(int,input().split()))
S = [input() for _ in range(K)]
# cate_id = 
# 132534
#1-->N, cate[0]-->cate[N-1]

dp = [[float('inf')]*K for _ in range(K)] 
for i in range(K):
    for j in range(K):
        if S[i][j] == '1':
            dp[i][j] = abs(cate[i]-cate[j])
