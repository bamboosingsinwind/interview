from collections import defaultdict

def preprocess_lca(tree, root):
    n = len(tree)
    log_n = (n - 1).bit_length()
    parent = [[-1] * n for _ in range(log_n)]
    depth = [-1] * n
    depth[root] = 0
    stack = [root]
    while stack:
        node = stack.pop()
        for child in tree[node]:
            if depth[child] == -1:
                parent[0][child] = node
                depth[child] = depth[node] + 1
                stack.append(child)
    for k in range(1, log_n):
        for node in range(n):
            if parent[k - 1][node] != -1:
                parent[k][node] = parent[k - 1][parent[k - 1][node]]
    lca = defaultdict(lambda: defaultdict(int))
    for u in range(n):
        for v in range(u + 1, n):
            if depth[u] > depth[v]:
                u, v = v, u
            diff = depth[v] - depth[u]
            for k in range(log_n):
                if diff & (1 << k):
                    v = parent[k][v]
            if u == v:
                lca[u][u] += 1
            else:
                for k in range(log_n - 1, -1, -1):
                    if parent[k][u] != parent[k][v]:
                        u = parent[k][u]
                        v = parent[k][v]
                lca[u][v] += 1
                lca[v][u] += 1
    return lca

def count_paths(lca, a, b, c, d):
    ab_lca = lca[a][b]
    cd_lca = lca[c][d]
    ac_lca = lca[a][c]
    bd_lca = lca[b][d]
    ad_lca = lca[a][d]
    bc_lca = lca[b][c]
    abd_lca = lca[a][b] + lca[a][d] - lca[a][c] - lca[b][c]
    acb_lca = lca[a][c] + lca[a][b] - lca[a][d] - lca[c][d]
    return ab_lca * cd_lca - ac_lca * bd_lca + abd_lca - acb_lca
n, m = map(int, input().split())
tree = [[] for _ in range(n)]
for i, parent in enumerate(map(int, input().split())):
    tree[parent - 1].append(i + 1)
lca = preprocess_lca(tree, 0)
for i in range(m):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(count_paths(lca, a, b, c, d))