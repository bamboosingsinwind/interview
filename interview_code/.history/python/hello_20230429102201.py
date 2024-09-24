import numpy as np

5 2 4
1 2 2 1 1
1 0 0 0 0
0 0 1 1 1
0 0 0 0 1
0 0 1 0 1
1 0 0 1 1
0 1 0 0 0
2 2 3
2 3 2
2 3 1
1 2 4
n,m,q = (int(i) for i in input().split(" "))
cls_dep = [int(i) for i in input().split(" ")]
f_in = input().split("\n") #int(j) for j in i.split(" ") 
f = [int(j) for j in i.split(" ") for i in f_in ]
