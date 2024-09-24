
def partition(arr, low, high): #
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickselect(arr, k):
    low = 0
    high = len(arr) - 1
    while True:
        pivot_index = partition(arr, low, high)
        if pivot_index == k-1:
            return arr[pivot_index]
        elif pivot_index < k-1:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

def k_element(arr, k):
    return quickselect(arr, k)

arr = [3,1,2,4]
print(k_element(arr,3))
    