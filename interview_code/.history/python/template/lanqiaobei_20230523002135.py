# https://blog.csdn.net/weixin_63003502/article/details/129968532
#%%

#前缀和:处理等差数列，等比数列
a = [0] + list(map(int,input().split()))
n = len(a) - 1
s = [0]*(n+1)
for i in range(1,n+1):
    s[i] = s[i-1] + a[i]
# sum[l,r]
l,r = 1,3
print(s[r]-s[l-1])
#%%
#二分法
def bisearch(arr,target):
    l,r = 0,len(arr)-1
    while l<=r:#对于可能不存在的，此处含=，最后返回-1；若必定存在，则可不含=，最后返回l
        m = (l+r)//2
        if(arr[m]==target):return m
        elif (arr[m]>target):
            r = m - 1
        else:
            l = m + 1
    return -1 # no found
#%%
#快速排序及其组件
def quicksort(arr):#python版快排
    n = len(arr)
    if n < 2:return arr
    p = arr[0]
    less,greater = [],[]
    for i in arr[1:]:
        if i>p:
            greater.append(i)
        else:
            less.append(i)
    return quicksort(less) + [p] + quicksort(greater)

#cpp版快排及组件
def partition(arr,l,r):
    p = arr[l]
    while l<r:
        while l<r and arr[r]>=p: r -= 1
        arr[l] = arr[r] #保护谁，替换谁。arr[l]赋值给p被保护后，首先替换掉arr[l]
        while l<r and arr[l]<p: l += 1
        arr[r] = arr[l]
    arr[l] = p
    return l 

def quicksort_cpp(arr,l,r):#l=0,r=n-1
    if l<r:#切记！！！此处是if，不是while
        mid = partition(arr,l,r)
        quicksort_cpp(arr,l,mid-1) 
        quicksort_cpp(arr,mid+1,r)
arr = [3,1,4,2]        
quicksort_cpp(arr,0,3)  
print(arr) 
#双指针：左右指针，快慢指针
for i in range(n):#i快指针
    j = 0
    while j<i and check(j):#j是慢指针，满足条件后才移动
        j += 1
 
# %%
#位运算： 求十进制n的二进制第k位
n>>k&1
#lowbit(x) 返回x的最后一位1（二进制下的） x = 1010（二进制），lowbit（x） = 10（二进制） = 2（十进制）

#%%
#最大公约数&最小公倍数
def gcd(a,b):
    while b:#while的是b，返回的是a
        a,b = b,a%b
    return a
def lmc(a,b):
    s = a*b
    while b:
        a,b = b,a%b
    return s//a

#%%
#判断质数和埃氏筛法模板
def prime(x):
    for i in range(2,int(x**0.5)+1):#2开始，根号后要+1
        if x%i ==0:
            return False
    return True
def aishi_prime(x):
    maxn = 10000
    is_prime = [True for _ in range(maxn)]
    prime = []
    for i in range(2,maxn):
        if is_prime[i]:
            prime.append(i)
            for j in range(i,maxn,i):#划掉i的倍数
                is_prime[j] = False       
# %%
#唯一分解定理：每个大于1的自然数均可写为质数的积，而且这些素因子按大小排列之后，写法仅有一种方式。如：n>1，n=(2^a)*(3^b)*(5^c)…*(x^y)
#推论：n的约数个数=(a+1)(b+1)…(y+1)，（求出数n的因子个数）
def decomp(x):
    i = 2
    res = []
    while i<=x:
        if x%i == 0:
            res.appen(i)
            x //= i
        else:
            i += 1
    return res
#%%
# 快速幂 (a * b) % p = (a % p * b % p) % p , (a + b) % p = (a % p + b % p) % p ，(a - b) % p = (a % p - b % p) % p 
def fast_pow(a,b,p):
    ans = 1
    a %= p
    while b:
        if b%2 ==1:
            ans = (ans * a) % p
        a = (a * a) % p
        b >>= 1
    return ans

#%%
# 并查集:集合合并；询问2个元素是否在同一个集合中
def find(x):#返回x的祖宗
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x,y):
    if find(x)!= find(y): #合并x,y为同一家族
        p[find(y)] = find(x) #将y的祖史加入x的祖史中来。 这个操作是可行的，但不好理解。 有时候合并不是必需的，甚至可以将x合并到y的祖史中去除合并的情况。 如果x和y都是家族的话，合并将更加复杂（甚至可以少于两次）。 如果x和y都是偶数怪，合并将有时称为冰雹
# p[N]存储每个点的祖宗节点，索引为当前节点，当前节点的值代表当前节点的祖宗
p = [i for i in range(1,N+1)] #初始化，假定节点编号是1~n

#%%
#区间合并：贪心的策略去解决，不是按照左端点排序，就是按照右端点排序，或者按照左右端点双关键字排序。这里我们按照左端点进行排序的，本质其实还是判断重叠区间问题
def merge(intervals):
    if len(intervals)==0: return intervals
    intervals.sort(key=lambda x:x[0])
    res = []
    res.append(intervals[0])
    for i in range(1,len(intervals)):
        last = res[-1]
        if last[1]>=intervals[i][0]:
            res[-1][1] = max(last[1], intervals[i][1]) 
        else:
            res.append(intervals[i])    
    return res
#%%
# 回溯
# 介绍：回溯的本质是穷举，穷举所有可能，然后选出我们想要的答案，比如下面的深搜也是回溯的一种。
# 思想：溯法解决的问题都可以抽象为树形结构，集合的大小就构成了树的宽度，递归的深度，都构成的树的深度。
# for循环可以理解是横向遍历，backtracking（递归）就是纵向遍历
# 一般可以解决如下几种问题：
# 1.组合问题：N个数里面按一定规则找出k个数的集合
# 2.切割问题：一个字符串按一定规则有几种切割方式
# 3.子集问题：一个N个数的集合里有多少符合条件的子集
# 4.排列问题：N个数按一定规则全排列，有几种排列方式
# 5.棋盘问题：N皇后，解数独等等
def backtrack(param):
    if (终止条件):
        存放结果
        return
    for (选择:本层集合中元素（树中节点孩子的数量就是集合的大小)):
        处理节点
        backtrack(路径，选择列表) 
        回溯，撤销处理结果
#%%
def dfs(param):
    if (越界不合法):return
    if (重点边界):
        输出结果
        return
    for(枚举所有方案):
        if(未标记):
            标记
        dfs(下一层)
        撤销标记，回溯
from collections import deque#双端队列 popleft,append,len(q)
def bfs(graph,root):#
    q = deque()
    q.append(root)
    seen = set()
    seen.add(root)
    while q:
        node = q.popleft()
        next_list = graph[node]
        for no in next_list:
            if no not in seen:
                q.append(no)
                seen.add(no)
#%%
edge = [] #edge[i] = a,b,w
edge.sort(key=lambda x:x[2])
res = 0
cnt = 0
for x in edge:
    a,b,w = x
    if find(a)!=find(b) and cnt < n-1:#a-b不连通 and 边数<n-1
        res += w
        union(a,b)
        j += 1

#%%
# 拓扑排序：有向图，检测环，有向无环图一定有拓扑序列
graph = { 'a':'bf', 'b':'cdf','c':'d','d':'ef','e':'f'} # node:next_list
def topsort(graph):
    indegree = dict((i,0) for i in graph.keys())
    for i in graph.keys():
        for j in graph[i]:
            indegree[j] += 1 	#indegree of each node is number of edges pointing to it.
    stack = [i for i in indegree.keys() if indegree[i]==0]
    seq = []
    while stack:
        node = stack.pop()
        seq.append(node)
        for k in graph[node]:
            indegree[k] -= 1
            if 	indegree[k] == 0: 	# if neighbor's indegree becomes zero, add it to the stack.
                stack.append(k)
    if len(seq) == len(indegree):#无环，输出排序
        print(seq)
    else:
        print("circle")#有环，不存在拓扑排序。

#%%
# 最短路径
#https://blog.csdn.net/time_money/article/details/109899692
def dijkstra(network, s, d):  # 迪杰斯特拉算法算s-d的最短路径，并返回该路径和值
    path = []  # 用来存储s-d的最短路径
    n = len(network)  # 邻接矩阵维度，即节点个数
    fmax = float('inf')
    w = [[0 for _ in range(n)] for j in range(n)]  # 邻接矩阵转化成维度矩阵，即0→max

    book = [0 for _ in range(n)]  # 是否已经是最小的标记列表
    dis = [fmax for i in range(n)]  # s到其他节点的最小距离
    book[s - 1] = 1  # 节点编号从1开始，列表序号从0开始
    midpath = [-1 for i in range(n)]  # 上一跳列表
    for i in range(n):
      for j in range(n):
        if network[i][j] != 0:
          w[i][j] = network[i][j]  # 0→max
        else:
          w[i][j] = fmax
        if i == s - 1 and network[i][j] != 0:  # 直连的节点最小距离就是network[i][j]
          dis[j] = network[i][j]
    for i in range(n - 1):  # n-1次遍历，除了s节点
      min = fmax
      for j in range(n):
        if book[j] == 0 and dis[j] < min:  # 如果未遍历且距离最小
          min = dis[j]
          u = j
      book[u] = 1
      for v in range(n):  # u直连的节点遍历一遍
        if dis[v] > dis[u] + w[u][v]:
          dis[v] = dis[u] + w[u][v]
          midpath[v] = u + 1  # 上一跳更新
    j = d - 1  # j是序号
    path.append(d)  # 因为存储的是上一跳，所以先加入目的节点d，最后倒置
    while (midpath[j] != -1):
      path.append(midpath[j])
      j = midpath[j] - 1
    path.append(s)
    path.reverse()  # 倒置列表
    print("path:",path)
    # print(midpath)
    print("dis:",dis)
    # return path
# folyd https://blog.csdn.net/JohnJim0/article/details/109156986
def floyd(adjacent_matrix):
    vnum = len(adjacent_matrix)
    a = [[adjacent_matrix[row][col] for col in range(vnum)] for row in range(vnum)]
    nvertex = [[-1 if adjacent_matrix[row][col]==float('inf') else col for col in range(vnum)] for row in range(vnum)]
    # print(adjacent_matrix)
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j]>a[i][k]+a[k][j]:
                    a[i][j]=a[i][k]+a[k][j] 
                    nvertex[i][j] = nvertex[i][k]
    return nvertex, a

adjacent_matrix = graph2adjacent_matrix(graph)
nvertex, a = floyd(adjacent_matrix)
#%%
# 01背包 dp
# 1.确定dp数组（dp table）以及下标的含义
# 2.确定递推公式
# 3.dp数组如何初始化
# 4.确定遍历顺序
# 5.举例推导dp数组
def test01():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    # 初始化: 全为0
    dp = [0] * (bag_weight + 1)
    # 先遍历物品, 再遍历背包容量
    for i in range(len(weight)):
        for j in range(bag_weight, weight[i] - 1, -1):
            # 递归公式
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp)
test01()


  


      
        