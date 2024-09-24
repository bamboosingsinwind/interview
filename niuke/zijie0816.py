from collections import deque
def solve(ss):
    def helper(s):
        num = 0
        res = ""
        while len(s):
            c = s.popleft()
            if c.isdigit():
                num = num*10 +int(c)
                continue
            if c == '[':
                res += helper(s)*num
                num = 0
            if c.isalpha():
                res += c
            if c == ']':
                num = 0
                break
        return res
    return helper(deque(ss))
print(solve("2[jk]e1[f]ef"))
    

