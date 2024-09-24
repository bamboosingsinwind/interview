num = input().lstrip()
print(num)
def fun(num):
    if num[0] !='+' and num[0] != '-' and (not num[0].isdigit()):
        return 0
    elif num[0] == '+':
        res = int(num[1:])
        res = min(res,2**31-1)
    elif num[0].isdigit():
        res = int(num)
        res = min(res,2**31-1)
    else:
        res = int(num[1:])
        res = -min(res,2**31)
    return res
print(fun(num))