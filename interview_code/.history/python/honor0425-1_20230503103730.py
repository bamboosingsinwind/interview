num = input().lstrip()
def fun(num):
    if num[0] !='+' or num[0] != '-':
        return 0
    
    elif num[0] == '+':
        res = int(num[1:])
        res = min(res,2**31-1)
    else:
        res = int(num[1:])
        res = -min(res,2**31)
    return res
print(fun(num))