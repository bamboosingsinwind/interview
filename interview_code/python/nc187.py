def compressString(s: str, k: int) -> int:
    # write code here
    def count(ss):
        ss += "#"
        line = ""
        alp = ss[0]
        cnt = 0
        for i in range(len(ss)):
            if ss[i] == alp:
                cnt += 1
            else:
                line += alp
                if cnt > 1:
                    line += str(cnt)
                alp = ss[i]
                cnt = 1
        return len(line)
      
    n = len(s)
    res = count(s)
    for i in range(1,k+1):
        for j in range(n-i):
            ss = s[:j] + s[j+i:]
            res = min(res,count(ss))
    return res
s,k = "aaabcccd",2
print(compressString(s,k))
