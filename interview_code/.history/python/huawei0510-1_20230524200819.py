li = [10,20,50,80,1,1]#[6,1,2,3] 
def check(st,i):
    if len(st)==0:
        return st,i
    else:
        su = sum(st) + st[0]
        for j in range(len(st)):
            su -= st[j]
            if i == #sum(st[j:]):
                st = st[:j]
                i = i*2 
                # break
    return st,i
def st_combine(li):
    st = []
    for i in li:
        st,n1 = check(st,i)
        while n1!=i:
            i = n1
            st,n1 = check(st,i)
        st.append(n1)
    return st
print(st_combine(li)) 