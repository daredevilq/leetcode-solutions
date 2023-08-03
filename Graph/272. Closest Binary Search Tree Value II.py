from queue import PriorityQueue

class BST_Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None  

def maximum(root):
    while root.right is not None:
        root = root.right
    return root

def minimum(root):
    while root.left is not None:
        root = root.left
    return root

def successor(root):
    if root.right is not None:
        return minimum(root.right)
    p_root = root.parent
    while root:
        if not p_root.left:
            root = p_root
            p_root = root.parent
    return p_root


def predecessor(root):
    if root.left is not None:
        return maximum(root.left)
    p_root = root.parent

    while root:
        if root != p_root.right:
            root = p_root
            p_root = root.parent
    return p_root

def find_node(tree, target):
    bestnode = tree
    min_diff = abs(tree.val - target)

    def dfs(node):
        nonlocal min_diff
        nonlocal bestnode
        if node is None:
            return
        if abs(node.val - target) < min_diff:
            min_diff = abs(node.val - target)
            bestnode = node
        dfs(node.left)
        dfs(node.right)

    return bestnode



def closest_values(tree, target, k):
    best_node = find_node(tree, target)
    succ = successor(best_node)
    pred = predecessor(best_node)



    result = []
    result.append(best_node.val)
    result.append(succ)
    result.append(pred)

    for i in range(k):
            succ = successor(succ)
            pred = predecessor(pred)
            result.append(succ.val)
            result.append(pred.val)
    return result



def closeest_value_heap(tree, target, k):
    queue = PriorityQueue()
    no_of_nodes = 0

    def dfs(node):
        nonlocal no_of_nodes
        


A = BST_Node(4)
B = BST_Node(2)
C = BST_Node(5)
D = BST_Node(1)
E = BST_Node(3)
A.left = B
A.right = C
B.left = D
B.right = E
B.parent = A
C.parent = A
D.parent = B
E.parent = B

print(closest_values(A, 3.714286, 2))