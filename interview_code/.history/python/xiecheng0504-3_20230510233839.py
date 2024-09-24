# 11~ ,~~~
string = [s for s in input() ]
def check(str):
    n = len(str)
    
    if n<3: return True
    
    for i in range(n-1):
        if str[i] == str[i+1] and str[i]!='?':
            return False

    for i in range(len(str)-2):
        cnt = str[i:i+3].count('1')
        if cnt % 2: return False   # odd counts are not minimal strings
    return True
pos = list("012")
# 截取?前后，进行切分不含？的一次性check
#然后对截取?前后进行递归回溯，check
res = ""
def recursion(string,id,pos):
    if id >= len(string): return "".join(string)
    # loc = string.find("?")
    for s in string:
        if s != '?':
            res += s
        
print(check(str))           
    
        