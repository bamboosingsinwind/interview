words = input().split(',')
L = int(input())

def fun(words,L):
    #递归，最后一行的判断
    line = []
    line_len = 0
    if(len(words)<1):return
    for i,word in enumerate(words):
        if line_len + len(word) < L:
            line.append(word)  
            line_len += len(word) 
        else:
            break
    if i == len(words)-1:
        print("*".join(line).ljust(width=L,fillchar="*"))
    else:
        words = words[i:]
        if len(line)==1:print(line[0].ljust(width=L,fillchar="*"))
        else:
            star = (L-line_len)//(len(line)-1)
            remain = (L-line_len)%(len(line)-1)
            for j in range(min(remain,len(line))):
                line[j] +='*'
            res = ("*"*star).join(line)
            print(res)
        fun(words,L)
fun(words,L)
        
        
        