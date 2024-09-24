
def check(hash,t_hash):
    for k,v in t_hash.items():
        if hash[k] < v:
            return 0
    return 1
def minWindow(  s: str, t: str) -> str:
    # write code here
    n = len(s)
    i,j = 0,0
    hash = {k:0 for k in t}
    t_hash = {}
    for val in t:
        if val not in t_hash:
            t_hash[val] = 1
        else:
            t_hash[val] += 1
    res = s
    while j < n:
        while j<n and not check(hash,t_hash):
            if s[j] in hash:
                hash[s[j]] += 1
            j += 1
        while check(hash,t_hash):
            if s[i] in hash:
                hash[s[i]] -= 1
            i += 1
        if j-i+1 < len(res):
            res = s[i-1:j] 
    hash = {k:0 for k in t}
    for val in s:
        if val in hash:
            hash[val] += 1
    if not check(hash,t_hash):
        return ""
    return res

print(minWindow("ADOBECODEBANC","ABC"))