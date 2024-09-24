def FindContinuousSequence( sum: int):
        # write code here
        if sum < 1:return []
        l,r = 1,1
        temp = 1
        res = []
        while r<sum:
            if temp == sum:
                if r - l > 0:
                    res.append(list(range(l,r+1)))
                r += 1
                temp += r
            elif temp > sum:
                temp -= l
                l += 1
            else:
                r += 1
                temp += r
        return res
print(FindContinuousSequence(9))
