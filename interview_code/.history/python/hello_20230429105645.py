import numpy as np

n,m,q = (int(i) for i in input().split(" "))
cls_dep = [int(i) for i in input().split(" ")]
f_in = []
for i in range(4):
     f_in.append(list(map(int, input().split(" "))))

g_in = []
for i in range(m):
     g_in.append(list(map(int, input().split(" "))))

q_in = []
for i in range(q):
     q_in.append(list(map(int, input().split(" "))))

def fun(a,b,c):#dep year cls
    if(f_in[b][c]==1 and g_in[b][c]==1):
        print("Help yourself")
    elif(cls_dep[c]==a):
        print("Ask for help") 
    else:
        print("Impossible")
for it in q_in:
    a,b,c = it[0]-1,it[1]-1,it[2]-1  #a dep year b class c year
    fun(a,b,c)