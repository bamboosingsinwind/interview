#最长无重复子串
from collections import defaultdict
s = "abbcdefde"
s2 = "xtcvvacdf"
def nodup(s):
    hash = defaultdict(int)
    n = len(s)
    res = 0
    if n<2: return n
    i = -1
    for j in range(n):
        while hash[s[j]]!=0:
            i += 1
            hash[s[i]] -= 1
        hash[s[j]] += 1
        res = max(res,j-i)
    return res
print(nodup(s))