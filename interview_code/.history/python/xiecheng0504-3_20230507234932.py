# 11~ ,~~~
str = input()
def check(str):
    n = len(str)
    pos = list("012")
    if n<3: return False, 'Not a minimal string'
    
    for i in range(n-1):
        if str[i] == str[i+1] and str[i]!='?':
            return "-1"
    sp = str.split('?')
    for s in sp:
        if(len(s)>2):
            for i in range(len(s)-2):
                cnt = s[i:i+3].count('1')
                if cnt % 2: return '-1'    # odd counts are not minimal strings
    res = ""
    for i in range(len(sp)-1):
        se = set(pos)-{sp[i][-1],sp[i+1][0]}
        cnt1 = (sp[i][-1]+sp[i+1][0]).count('1')
        if cnt1 != 1:
            se -= {'1'}
        se = list(se)
        if len(se) == 0: return '-1' # no overlap, not minimal string
        else:
            res += sp[i] + se[0] + sp[i+1]
    return res
print(check(str))           
    
        