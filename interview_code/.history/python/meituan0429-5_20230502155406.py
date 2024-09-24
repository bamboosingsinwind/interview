n,m = list(map(int,input().split()))
f = list(map(int,input().split()))
us = list(map(int,input().split()))
vs = list(map(int,input().split()))

f_map = {}#node-->parent
nxs = [[] for _ in range(n+1)] #save bi-edges
for i in range(n-1):
    nxs[i+2].append(f[i])
    nxs[f[i]].append(i+2) #reverse bi-edges for each edge (u,v in nxs[i+2]
    f_map[i+2] = f[i]
dp = {} #node pre-->延伸的节点数
def dfs(node,pre):
    if (node,pre) in dp: return dp[node,pre] #already calculated? 返回值是已经计算过的node的pre
    cur = 1
    for nx in nxs[node]:
        if nx != pre:
            cur += dfs(nx,node) #recurse on all children of node, including node itself, which is the parent of all children. 计
    dp[(node,pre)] = cur
    return cur

for i in range(m):
    ai,fi = us[i],f_map[us[i]]
    bi,gi = vs[i],f_map[vs[i]]  
    p1,p2 = -1,-1
    pf1,pf2 = -1,-1
    #合并为头对头的边
    if ai==bi:
        p1,pf1 = ai,fi
        p2,pf2 = fi,ai
    elif fi==gi:
        p1,pf1 = ai,fi
        p2,pf2 = bi,fi
    elif ai==gi:
        p1,pf1 = fi,ai
        p2,pf2 = bi,ai
    elif fi==bi:
        p1,pf1 = ai,fi
        p2,pf2 = gi,fi
    s1,s2 = dfs(p1,pf1), dfs(p2,pf2) #s1,s2 is the sum of the depths of the two nodes. 计算出
    print(s1*s2,end=" ")
    