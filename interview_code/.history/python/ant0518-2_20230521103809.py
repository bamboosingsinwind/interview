q = int(input())
# up,right,down,left  1convex -1concave
dic = {"W":[1,1,-1,1],"D":[1,1,1,-1],"S":[-1,1,1,1],"A":[1,-1,1,1]}
def solve(arr,r,c):
    for i in range(r):
        for j in range(c-1):
            if arr[i][j] != "*" and arr[i][j+1]!= "*":
                
        
    
   
    
for i in range(q):
    row,col = map(int,input().split())
    