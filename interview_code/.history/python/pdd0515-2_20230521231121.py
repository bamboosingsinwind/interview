T = int(input())
import numpy as np
def solve(large):
    res = []
    for i in large:
        if i[0]==i[1]:
            return -1
        if i[0] in res and i[1] in res:#顺序不乱
            
        elif i[0] in res:#最后一个
            if i[0] != res[-1]:#判定关系
                if 
            else:res.append(i[1])
        elif i[1] in res:#第一个
            if i[1]!= res[0]:return -1
            res = [i[0]] + res
        else:#2个都不在
            res +=[i[0]]+[i[1]]
def solve1(large):
    large = np.array(large)
    cha = large[-1]
    large.pop()
    while len(large):
        if cha[-1] in large[:,0]:
            id = large.index(cha[-1])
            cha.append(large[id][1])
            large.pop(id)
        elif cha[0] in large[:,1]:
            id = large.index(cha[0])
            cha.insert(0,large[id][0])
            large.pop(id)
        else:
            return -1

                    
for _ in range(T):
    N,M = map(int,input().split()) 
    large = []
    eq = {}
    for i in range(M):
        a,b,c = input().split()
        if b == '=':
            if c in eq.values:
                a,c = c,a
            if a not in eq:
                eq[c] = a
            else:
                eq[c] = eq[a]
        elif b == '>':
            if a in eq:a = eq[a]
            if c in eq:c = eq[c]
            large.append([a,c])
        else:
            if a in eq:a = eq[a]
            if c in eq:c = eq[c]
            large.append([c,a])
        