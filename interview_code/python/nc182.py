from collections import defaultdict

def wordDiv(s: str, dic):
    # write code here
    res = []
    # dic.sort()
    hash = defaultdict(list)
    for i in dic:
        hash[i[0]].append(i)
    line = []
    def recursion(id,line,s):
        if id >= len(s):
            if id == len(s):
                res.append(" ".join(line))
            return
        for i in hash[s[id]]:
            id += len(i)
            line.append(i)
            recursion(id,line,s)
            line.pop()
            id -= len(i)
    recursion(0,line,s)
    return res
s,dic = "aaaaaaaaaaaaaaaaaaaa",["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa"]
print(wordDiv(s, dic))