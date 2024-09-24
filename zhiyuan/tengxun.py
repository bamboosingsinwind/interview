class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
res = 0
def solve(root,temp):
    if root:
        if root.left==None and root.right==None:
            global res
            res += temp
            return
        solve(root.left,10*temp+root.value)
        solve(root.right,10*temp+root.value)
# root = 
# solve(root,0)
# print(res)





