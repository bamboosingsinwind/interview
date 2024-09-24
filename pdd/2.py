from math import ceil
print(ceil(131/0.12))
n,k = 5,12
arr = [1000,34,12,27,131]
def solve(n,k,arr):
    res = 0
    cur = 0
    arr1 = [ceil(100*i/k) for i in arr[1:]]
    arr_sum = []
    for i in arr[:-1]:
        cur += i
        arr_sum.append(cur)
    print(arr1)# need
    print(arr_sum) #in fact
    for i in range(n-1):
        if arr1[i] > arr_sum[i]:
            res += (arr1[i] - arr_sum[i])
    print(res)
solve(n,k,arr)