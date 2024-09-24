# 11~ ,~~~
str = input()
def check(str):
    n = len(str)
    if n<3: return False, 'Not a minimal string'
    
    for i in range(n-1):
        if str[i] == str[i+1] and str[i]!='?':
            return "-1"
    
    
        