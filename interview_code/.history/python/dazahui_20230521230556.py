import time
a = list(range(100000000))
t0 = time.time()
a.insert(0,-1)
t1 = time.time()
print("insert time",t1-t0)
a = a[1:]
t2 = time.time()
a = [-1] + a
print("add front time ",time.time()-t2)