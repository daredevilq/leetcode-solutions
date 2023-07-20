# Definition for a binary tree node.
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    
class Solution:
    def maxSumBST(self, root):
        
        def check_if_bst(node, previous_val, come_from):
            if node == None:
                return 0

            if node.val > previous_val and come_from == "left":
                return -inf

            if node.val < previous_val and come_from == "right":
                return - inf

            

            summary = node.val + check_if_bst(node.left, node.val, "left") + check_if_bst(node.right, node.val, "right") 
            return summary

        best_sum = -1
        def tree_sum(node):
            nonlocal best_sum
            if node == None:
                return
            
            best_sum = max(best_sum, check_if_bst(node, 0, 0, node.val))

            tree_sum(node.left)
            tree_sum(node.right)
        
        tree_sum(root)
        return max(0, best_sum)
    

A = TreeNode()
B = TreeNode()
C = TreeNode()
D = TreeNode()
E = TreeNode()
F = TreeNode()
G = TreeNode()
H = TreeNode()
I = TreeNode()

A.left = B
A.right = C
A.val = 1

B.left = D
B.right = E
B.val = 4

C.left = F
C.right = G
C.val = 3

D.val = 2
E.val = 4
F.val = 2

G.val = 5
G.left = H
G.right = I

H.val = 4
I.val = 6

sol = Solution()
print(sol.maxSumBST(A))