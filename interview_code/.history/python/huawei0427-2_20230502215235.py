s1 = input()
s2 = input()
k = int(input())
res = -1

from collections import Counter
cnt1 = Counter(s1)#转化为字典{key:count}
cnt2 = Counter(s2[:len(s1)+k])

def check(cnt1,cnt2):
    for s in cnt1:
        if s not in cnt2 or cnt1[s]>cnt2[s]:
            return False
    return True
if check(cnt1,cnt2):
    res = 0
else:
    for l in range(1,len(s2)-k+1):
        cnt2[s2[l]] -= 1
        r = l +len(s1)+k
        if s2[r] not in cnt2:
            cnt2[s2[r]] = 0
        cnt2[s2[r]] += 1
        if check(cnt1,cnt2):
            res = l
            break
print(res)   
