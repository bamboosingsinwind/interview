from collections import defaultdict
tree = defaultdict(list)
n = int(input())
for _ in range(n-1):
    a,b = list(map(int,input().split(" ")))
    tree[a].append(b)
de = int(input())

def count_child(tree,node):
    res = 1
    if len(tree[node]) == 0:return res
    child = tree[node]
    for no in child:
        res += count_child(tree,no)
    return res
def fun(tree,de,n):
    num = 0
    lst = []
    if len(tree[de])==0:
        if n > 1:
            num = 1
            lst.append(n-1)
    else:
        num = len(tree[de])
        for i in tree[de]:
            lst.append(count_child(tree,i))
        rest = n - 1 - sum(lst)
        if rest:
            num += 1
            lst.append(rest)
    lst.sort()
    print(num)
    for i in lst:
        print(i,end=" ")
fun(tree,de,n)