def minJumpStep(nums) -> int:
        # write code here
        n = len(nums)
        if n==0:return -1
        dp = [-10000]*n
        dp[0] = 0
        s = 0

        dpr = [0]*n 	# save the previous row, for backtracking
        dpr[0] = nums[0]
        for i in range(1,n):
            while nums[s] + s < i:
                s+=1
            if dp[s] >=0:
                dp[i] = dp[s] + 1
                dpr[i] = dpr[s] + 
        return dp[-1] if dp[-1]>0 else -1
print(minJumpStep([2,4,2,1,0,100]))