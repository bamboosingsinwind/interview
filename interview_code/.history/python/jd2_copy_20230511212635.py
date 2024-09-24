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
    