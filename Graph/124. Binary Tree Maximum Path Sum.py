from math import inf
class TreeNode:
    def __init__(self,val = 0, left = None, right =None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def maxPathSum(self, root):
        memo = {}
        def recursion(node):
            if node == None:
                return 0
            
            if node in memo:
                return memo[node]

            result = -inf
            result = max(node.val, node.val + recursion(node.left), node.val + recursion(node.right) , node.val + max(recursion(node.left), recursion(node.right)))
            
            memo[node] = result
            return result

        answer = -inf

        def dfs(node):
            nonlocal answer
            if node == None:
                return
            answer = max(answer, node.val + recursion(node.left) + recursion(node.right), node.val, node.val + recursion(node.left), node.val + recursion(node.right))
            dfs(node.left,)
            dfs(node.right)

        dfs(root)
        return answer


A = TreeNode()
B = TreeNode()
C = TreeNode()
D = TreeNode()
E = TreeNode()

A.val = -10
A.left = B
A.right = C
B.val = 9
C.val = 20
C.left = D
C.right = E
E.val = 7
D.val = 15
sol = Solution()
print(sol.maxPathSum(A))