inp = [100,100,100,50,100,5,10]
# from pythonds import PriorityQueue
from queue import PriorityQueue
q = PriorityQueue(5)
for i in inp:
    q.put(i)
print(q)