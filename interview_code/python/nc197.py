# def canJump( nums) -> bool:
#     # write code here
#     n = len(nums)
#     dp = [0 for _ in range(n)]
#     dp[0] = 1
#     for i in range(n):
#         if dp[i] == 1 and nums[i] > 0:
#             for j in range(i+1,min(i+nums[i]+1,n)):
#                 dp[j] = 1
#     return dp[n-1] == 1
# canJump([3,0,6,2,0,0,1])

def minSubarray( nums, target) -> int:
        # write code here
        ma = sum(nums)
        if ma<target:
            return 0
        res = len(nums)
        i,j = 0,0
        cur = 0
        while i < len(nums):
            # cur += nums[i]
            while i < len(nums) and cur < target:
                cur += nums[i]
                i += 1
            if cur >= target:
                res = min(res,i-j)
            cur -= nums[j]
            j += 1
        return res
nums ,target = [1,2,4,4,1,1,1],9
print(minSubarray( nums, target))