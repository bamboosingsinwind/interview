li = [6,1,2,3] 
def check(st,i):
    flag = False
    if len(st)==0:
        st.append(i)
    else:
        for j in range(len(st)):
            if i == sum(st[j:]):
                flag = True
                st = st[:j]
                st.append(2*i)
        if not flag:
            st.append(i)
    
def st_combine(li):
    st = []
    for i in li:
        
        
        
    return st
print(st_combine(li)) 