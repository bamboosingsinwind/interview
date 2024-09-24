q = int(input())
# up,right,down,left  1convex -1concave
dic = {"W":[1,1,-1,1],"D":[1,1,1,-1],"S":[-1,1,1,1],"A":[1,-1,1,1]}
def solve(arr,r,c):
    for i in range(r):
        for j in range(c-1):
            if arr[i][j] != "*" and arr[i][j+1]!= "*":
                if dic[arr[i][j]][1] + dic[arr[i][j+1]][3] != 0:
                    return False
    for i in range(r-1):
        for j in range(c):
            if arr[i][j] != "*" and arr[i+1][j]!= "*":
                if dic[arr[i][j]][2] + dic[arr[i+1][j]][0] != 0:
                    return False
        
    
   
    
for i in range(q):
    row,col = map(int,input().split())
    