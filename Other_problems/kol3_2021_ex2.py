from math import inf

class BNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None






def cutthetree(T):


    def dfs(root):
        if root.left is None and root.right is None:
            return inf
        
        left = 0
        right = 0

        if root.left:
            left = dfs(root.left)
        if root.right:
            right = dfs(root.right)

        ans = min(left + right, root.value)
        return ans

    asnwer = dfs(T.left) + dfs(T.right)
    return asnwer



A = BNode(10)
B = BNode(3)
C = BNode(15)
D = BNode(-1)
E = BNode(11)
F = BNode(17)
G = BNode(-5)
H = BNode(0)

A.left = B
A.right = C
B.left = D
B.right = None
C.left = E
C.right = F
D.left = G
D.right = H

print(cutthetree(A))