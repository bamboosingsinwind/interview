def Jump(n: int, A) -> int:
        # write code here
        cur = 0
        res = 0
        nex = A[0]
        i = 0
        while i < n:
            res += 1
            cur = nex
            if nex >= n-1:
                return res 
            for j in range(i,cur+1):
                nex = max(nex,j+A[j])
                if nex >= n-1:
                    return res + 1
            i = cur + 1
        return res
print(Jump(3,[2,3,1]))