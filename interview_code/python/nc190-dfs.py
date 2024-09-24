def generatePermutation(s: str) :
    # write code here
    res = []
    def dfs(idx, t):
        nonlocal res
        if idx > len(s):
            return
        res.append("".join(t))
        for i in range(idx, len(s)):
            dfs(i + 1, t + [s[i]])
    dfs(0, [])
    print(res)
generatePermutation("abc")

def generatePermutation1(s: str) :
    # write code here
    res = []
    def dfs(idx, t):
        nonlocal res
        if idx == len(s):
            res.append("".join(t))
            return
        
        for i in range(idx, len(s)):
            dfs(idx + 1, t + [s[i]])
    dfs(0, [])
    print(res)
generatePermutation1("abc")