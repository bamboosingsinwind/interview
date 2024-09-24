# 11~ ,~~~
string = [s for s in input() ]
def check(str1):
    n = len(str1)
    
    # if n<3: return True
    
    for i in range(n-1):
        if str1[i] == str1[i+1] and str1[i]!='?':
            return False
    if n < 3: return True
    for i in range(len(str1)-2):
        cnt = str1[i:i+3].count('1')
        if cnt % 2: return False   # odd counts are not minimal strings
    return True
pos = list("012")
# 截取?前后，进行切分不含？的一次性check
#然后对截取?前后进行递归回溯，check
res = ""
def recursion(string,id,pos):
    
    # loc = string.find("?")
    global res
    if id >= len(string): return "".join(res)
    for s in string:
        if s != '?':
            res += s
            id += 1
            if id <len(string):continue
            else:return "".join(res)
        if not check(res):return "-1"
        # error = 0
        for i in pos:
            res += i
            start = max(0,id-2)
            if check(res[start:]):
                return recursion(string,id+1,pos)
            res = res[:-1]
        return "-1"
print(recursion(string,0,pos))           
    
        