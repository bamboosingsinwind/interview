def partition(arr,l,r):
    key = arr[r]
    less = []
    greater = []
    for i in arr[l:r]:
        if i < key:
            less.append(i)
        else:
            greater.append(i)
    return len(less)
def k_element(arr,k):
    l = 0
    r = len(arr) - 1
    while True:
        id = partition(arr,l,r)
        if id == len(arr) - k:
            return arr[id]
        elif id < len(arr) - k:
            l  = id + 1
        else:
            r = id -1
print(k_element([2,1,3,4],1))