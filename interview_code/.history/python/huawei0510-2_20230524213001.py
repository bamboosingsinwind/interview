
def solve(s,N,k):
    n = len(s)
    res = -1
    for i in range(3,13):
        for j in range(n-i+1):
            x = int(s[j:j+i])
            if k == "+":
                