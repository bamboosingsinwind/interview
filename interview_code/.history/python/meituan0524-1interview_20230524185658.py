#最长无重复子串
from collections import defaultdict
s = "abbcdefde"
def nodup(s):
    hash = defaultdict(int)
    n = len(s)
    res = 0
    if n<2: return n
    i = 0
    for j in range(n):
        if hash[s[j]]==0:
            hash[s[j]] += 1
            res = max(res,j-i+1)
        else:
            while hash[s[j]]!=0:
                i += 1
                hash[s[i]] -= 1
    return res
print(nodup(s))