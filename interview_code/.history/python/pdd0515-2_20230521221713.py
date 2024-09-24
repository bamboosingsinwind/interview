T = int(input())

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
        