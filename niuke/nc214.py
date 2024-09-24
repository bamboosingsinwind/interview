def partition( nums) -> bool:
        # write code here
        def recursion(num,k):
            if len(num) == 1:
                if num[0] == k:return True
                return False
            for i in range(len(num)):
                a = num.pop(i)
                if recursion(num,a+k):return True
                num.insert(i,a)
            return False
        return recursion(nums,0)
partition([9,2,10,2,3,7,15])