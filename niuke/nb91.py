from typing import List
class Solution:
    def back(self,res,nums,temp,id):
        print("temp",temp)
        if len(temp) == n:
            res.append(temp)
            print("result",res)
            return
        for i in range(id,len(nums)):
            temp.append(num)
            nums = nums[1:]
            self.back(res,nums,temp,n)
            nums = [temp.pop()] + nums
        
    def cow_permute(self , nums: List[int]) -> List[List[int]]:
        # write code here
        nums.sort(reverse=True)
        res = []
        temp =  []
        self.back(res,nums,temp,len(nums))
        return res
SO =Solution()
print(SO.cow_permute([7]))