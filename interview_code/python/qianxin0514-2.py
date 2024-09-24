inp = [100,100,100,50,100,5,10]
# from pythonds import PriorityQueue
from queue import PriorityQueue
q = PriorityQueue(5)
inp.sort(reverse=True)
for i in inp[:5]:
    q.put(i)
for i in inp[5:]:
    mi = q.get()
    q.put(mi+i)
print(q.get())