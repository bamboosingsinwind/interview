import time
a = list(range(10000000000))
t0 = time.time()
a.insert(0,-1)
t1 = time.time()
print("insert time",t1-t0)
a = [-1] + a
print("add front time ",time.time()-t1)