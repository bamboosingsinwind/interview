def partition1(arr,l,r):#左边小，右边大
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
def partition(arr,l,r):#左边小，右边大
    key = arr[l]
    while l<r:
        if arr[r] >= key and l<r:
            r -= 1
        else:
            arr[l] = arr[r]
        if arr[l] <= key and l<r:
            l += 1
        else:
            arr[r] = arr[l]
    arr[l] = key
    return l
def partition(arr, low, high): #左边小，右边大
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1            
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
print(k_element([2,1,3,4],2))