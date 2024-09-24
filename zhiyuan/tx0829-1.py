def canPartition(nums):
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target_sum = total_sum // 2
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    for num in nums:
        if num <= target_sum:  # 只处理小于等于目标和的数
            for j in range(target_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
    
    return dp[target_sum]

# 示例
nums = [3, 1, 1, 2, 2, -1]
result = canPartition(nums)
if result:
    print("可以将数组分为和相等的两个子数组")
else:
    print("无法将数组分为和相等的两个子数组")
