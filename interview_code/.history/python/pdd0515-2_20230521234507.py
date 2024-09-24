T = int(input())
import numpy as np

def solve1(large):#去重后延伸成一条链
    col0 = [i[0] for i in large]
    col1 = [i[1] for i in large]   
    max_len = len(set(col0+col1))
    cha = large[-1]
    large.pop()
    while len(col0):
        if cha[-1] in col0:
            id = col0.index(cha[-1])
            cha.append(col1[id])
           
            col0.pop(id)
            col1.pop(id)
        elif cha[0] in col1:
            id = col1.index(cha[0])
            cha.insert(0,col0[id])
            
            col0.pop(id)
            col1.pop(id)
        else:
            return -1
    if max_len == len(cha):return len(cha)
    else:return -1  
ans = []              
for _ in range(1):
    N,M = 3,2#map(int,input().split()) 
    large = []
    equ = {}
    flag = False
    matrix = ["1 = 2","2 > 3"]
    for i in range(M):
        a,b,c = matrix[i].split()#input().split()
        if b == '=':
            if c in equ.values():
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

        