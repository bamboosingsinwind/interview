def count_subsets_greater_than_target(arr, target):
    def backtrack(index, current_sum):
        if current_sum > target:
            return 1  # 当前子集满足条件，返回1
        if index == len(arr):
            return 0  # 已经遍历完所有元素，返回0
        
        # 选择当前元素或不选择当前元素
        include_count = backtrack(index + 1, current_sum + arr[index])
        exclude_count = backtrack(index + 1, current_sum)
        
        return include_count + exclude_count
    
    return backtrack(0, 0)

def solve(arr):
    res = []
    for i in range(len(arr)):
        target = -arr[i]
        arr1 = arr[:i] + arr[i+1:]
        count = 1 if arr[i] >=0 else 0
        count += count_subsets_greater_than_target(arr1, target)
        res.append(count)
    return res
# print(solve([-1,2,-3]))
import numpy as np
print(dir(np))
