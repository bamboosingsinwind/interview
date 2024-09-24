
def solve(s,N,k):
    n = len(s)
    res = -1
    for i in range(3,13):
        for j in range(n-i+1):
            x = int(s[j:j+i])
            if k == "+":
                if len(set(str(x+N))) == 1:
                    res = max(res,x)
            elif k == "-":
                if len(set(str(x-N))) == 1:
                    res = max(res,x)
            elif k == "*":
                if len(set(str(x*N))) == 1:
                    res = max(res,x)
    return str(res)
s,N,k = "139804444677899222",2,"*"
print(solve(s,N,k))                
                    
                