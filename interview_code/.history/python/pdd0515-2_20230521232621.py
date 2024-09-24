T = int(input())
import numpy as np

def solve1(large):#去重后延伸成一条链
    large = np.array(large)
    max_len = len(set(large.reshape(-1)))
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
    if max_len == len(cha):return len(cha)
    else:return -1  
ans = []              
for _ in range(T):
    N,M = map(int,input().split()) 
    large = []
    equ = {}
    flag = False
    for i in range(M):
        a,b,c = input().split()
        if b == '=':
            if c in equ.values:
                a,c = c,a
            if a not in equ:
                equ[c] = a
            else:
                equ[c] = equ[a]
        elif b == '>':
            if a == c:
                flag = True
                break
            if a in equ:a = equ[a]
            if c in equ:c = equ[c]
            large.append([a,c])
        else:
            if a == c:
                flag = True
                break
            if a in equ:a = equ[a]
            if c in equ:c = equ[c]
            large.append([c,a])
    if flag:ans.append(-1)#print("-1")
    else:
        ans.append(solve1(large))
        # print(solve1(large))
print(ans)

        