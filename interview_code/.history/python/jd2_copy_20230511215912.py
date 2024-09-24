def partition1(arr,l,r):
    key = arr[r]
    less = []
    greater = []
    for i in arr[l:r]:
        if i < key:
            less.append(i)
        else:
            greater.append(i)
    arr = arr[:l] + less + [key] + greater + arr[r:]
    return len(less) + l
def partition(arr,l,r):
    key = arr[l]
    while l<r:
        if arr[r] >= key:
            r -= 1
        else:
            arr[l],arr[r] = arr[r],arr[l]
        if arr[l] <= key:
            l += 1
        else:
            arr[l],arr[r] = arr[r],arr[l]
    arr[l] = key
    return l
              
def k_element(arr,k):
    l = 0
    r = len(arr) - 1
    while True:
        id = partition(arr,l,r)
        if id == len(arr) - k :
            return arr[id]
        elif id < len(arr) - k:
            l  = id + 1
        else:
            r = id -1
print(k_element([2,1,3,4],3))