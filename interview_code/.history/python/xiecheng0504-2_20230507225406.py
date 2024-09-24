n = int(input())
sa = [list(map(int,input.split())) for _ in range(n)]
sa = sorted(sa, key=lambda x: (x[2], x[1], x[0])) 