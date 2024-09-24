def feature_size(n,k,s,p):
    return (n-k+2*p)/s + 1
while True:
    n,k,s,p = map(int,input().split()) # n,k,p,s are the number of balls, the number
    print(feature_size(n,k,s,p))