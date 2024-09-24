# 11~ ,~~~

string = input()#[s for s in input() ]
def check(str):
    n = len(str)
    
    if n<3: return False
    
    for i in range(n-1):
        if str[i] == str[i+1] and str[i]!='?':
            return False

    for i in range(len(str)-2):
        cnt = str[i:i+3].count('1')
        if cnt % 2: return False   # odd counts are not minimal strings
    return True
pos = list("012")
#
def recursion(string,id,pos):
    if id >= len(string): return "".join(string)
    for i
print(check(str))           
    
        