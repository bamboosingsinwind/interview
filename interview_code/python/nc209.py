def findUnsortedSubarray(nums) -> int:
        # write code here
        n = len(nums)
        if n == 1:return 0
        i,j = 0,n-1
        while i<j and nums[i]<nums[i+1]:
            i += 1
        while i<j and nums[j-1]<nums[j]:
            j -= 1
        mi,ma = 10**5,-10**5
        if j > i+1:
            mi,ma = min(nums[i+1:j]),max(nums[i+1:j])
        
        while True:
            update = False
            while i>0 and nums[i]>mi:
                if nums[i] > ma:
                    ma = nums[i]
                    update = True
                i -= 1
            while j<n-1 and nums[i]<ma:
                if nums[j] < mi:
                    mi = nums[j]
                    update = True
                j += 1
            if not update:
                break
        print(i,j)
        return max(0,j - i - 1)
print(findUnsortedSubarray([2,6,4,8,10,9,15]))