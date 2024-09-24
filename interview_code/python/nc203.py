from collections import defaultdict
def change( target: int, nums) -> int:
    # write code here
 
    memo = defaultdict(int)
    def dp(tar,end):
        targ = tar
        if (tar,end) in memo:
            return memo[(tar,end)]
        if tar < 0 or end < 0:
            return 0
        if tar == 0:
            memo[(0,end)] = 1
            return 1
        if end == 0 and tar % nums[0]==0:
            memo[(tar,0)] = 1
            return 1
        res = dp(tar,end-1)
        while tar > 0:
            res += dp(tar-nums[end],end-1)
            tar -= nums[end]
        memo[(targ,end)] = res
        return res
    return dp(target,len(nums)-1)
# print(change(5,[1,2,4,5]))
# from collections import deque
# q = deque([1,2,1])
# print(set(q))
# print(len(q))
for i in range(5):
    print(i)
    i += 2