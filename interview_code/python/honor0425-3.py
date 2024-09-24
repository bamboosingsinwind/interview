words = input().split(',')
L = int(input())

def fun(words,L):
    #递归，最后一行的判断
    line = []
    line_len = 0
    if(len(words)<1):return#写递归，一定要有终止条件，养成习惯
    for i,word in enumerate(words):
        if line_len + len(word) < L:
            line.append(word)  
            line_len += len(word) 
        else:
            break
    if i == len(words)-1:#只有一个单词时特殊处理
        print("*".join(line).ljust(L,"*"))#不支持ljust(width=,fillchar=)写法，直接传参即可
    else:
        words = words[i:]
        if len(line)==1:
            print(line[0].ljust(L,"*"))
        else:
            star = (L-line_len)//(len(line)-1)
            remain = (L-line_len)%(len(line)-1)
            for j in range(min(remain,len(line))):
                line[j] +='*'
            res = ("*"*star).join(line)
            print(res)
        fun(words,L)
fun(words,L)
        
        
        