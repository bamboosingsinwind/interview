n,m,q = map(int,input().split())
s = map(int,input().split())
f = [list(map(int,input().split())) for _ in range(4)]
g = [list(map(int,input().split())) for _ in range(m)]
dep_year_cls = [list(map(int,input().split())) for _ in range(q)]
for a,b,c in dep_year_cls:
    dep,year,cl = a-1,b-1,c-1
    if f[year][cl] and g[dep][cl]:
        print("Help yourself")
    elif s[cl] == a:
        print("Ask for help")
    else:
        print("Impossible")
    