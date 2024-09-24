import numpy as np


n,m,q = (int(i) for i in input().split(" "))
cls_dep = [int(i) for i in input().split(" ")]
f_in = input().split("\n")  
f = [i.split(" ") for i in f_in ]
f = np.array(f,astype=int)

g_in = input().split("\n") 
g = [i.split(" ") for i in g_in ]
g = np.array(g,astype=int)

qq_in = input().split("\n") 
qq = [i.split(" ") for i in qq_in ]
qq = np.array(qq,astype=int)