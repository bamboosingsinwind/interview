N = int(input())
# A,B,C,A + B,A +C,B + C,A + B + C
# A,B,A + B,C,A +C,B + C,A + B + C
# 7--2 6--4 5--6 4--8
def check(cur):
    A, B, C, AB, AC, BC, ABC = cur
    cnt = 0
    for i in (A,B,C):
        if i: cnt += 1
    while cnt < 3:
        if not A:
            if ABC and BC:
                A = ABC - BC
                cnt += 1
            elif AB and B:
                A = AB - B
                cnt += 1
            elif AC and C:
                A = AC - C
                cnt += 1
        if not B:
            if ABC and AC:
                B = ABC - AC
                cnt += 1
            elif AB and A:
                B = AB - A
                cnt += 1
            elif BC and C:
                B = BC - C
                cnt += 1
        if not C:
            if ABC and AB:
                C = ABC - AB
                cnt += 1
            elif AC and A:
                C = AC - A
                cnt += 1
            elif BC and B:
                C = BC - B
                cnt += 1
    if not (A<=B<=C) or (AB and A + B != AB) or (AC and A + C != AC) or (BC and B + C != BC) or (ABC and A + B + C != ABC):
        return False
    return (A,B,C)

def dfs(index,i,num,cur,time):
    if i == num:
        res = check(cur)
        # nonlocal vst
        if res:
            vst.add(res)
        cur[2],cur[3] = cur[3],cur[2] 
        res = check(cur)
        if res:
            vst.add(res)
        return
    for j in range(index,7):
        cur[j] = time[i]
        dfs(j+1,i+1,num,cur,time)
        cur[j] = 0
vst = set()                    
def solve(num,time):
    dfs(0,0,num,[0]*7,time)
    ans.append(len(vst))
    vst = set()
    

ans = []   
for i in range(N):
    num = int(input()) 
    time = [int(i) for i in input().split()]
    solve(num,time)
print(ans)
    