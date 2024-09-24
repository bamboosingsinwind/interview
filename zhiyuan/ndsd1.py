


def lengthOfLIS( nums, repeat: int) -> int:
    def lower_bound(nums, x):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= x:
                right = mid
            else:
                left = mid + 1
        return left
    n = len(nums)
    t = [inf] * (n + 1)
    for i in range(n):
        v = nums[i]
        j = lower_bound(t, v)
        if j == len(t) - 1:
            t.append(v)
        else:
            t[j] = v
    return len(t) - 1