# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root):
        is_camera_installed = {}
        no_cameras_installed = 0
        no_vertices = 0
        def dfs(node, parent):
            nonlocal no_cameras_installed
            nonlocal no_vertices
            if node is None:
                return
            no_vertices +=1

            if parent in is_camera_installed:
                pass
            else:
                no_cameras_installed +=1
                is_camera_installed[node] = True
            
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        if no_vertices == 1:
            return 1

        return min(no_cameras_installed, no_vertices - no_cameras_installed)
    


sol = Solution()

A = TreeNode()
B = TreeNode()
C = TreeNode()
D = TreeNode()

a = TreeNode()
b = TreeNode()
c = TreeNode()
d = TreeNode()
e = TreeNode()


A.left = B
B.left = C
B.right = D

a.left = b
b.left = c
c.left = d
d.right = e

print(sol.minCameraCover(a))