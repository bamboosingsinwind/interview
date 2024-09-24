a,b = [int(i) for i in input().split()]
def expect(a,b):
    # aa ab ba aa
    res = 0.25*((4*a+b) + 2*(2*a+2*b)+(a+4*b)) 
    print("%.2f"% res)
expect(a,b)