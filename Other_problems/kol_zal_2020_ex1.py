class Node:
    def __init__(self):
        self.left   = None  # lewe poddrzewo
        self.right  = None  # prawe poddrzewo
        self.parent = None  # rodzic drzewa (jeśli istnieje)
        self.value  = None  # przechowywana wartość



def sort_bts(root):
    arr = []

    def dfs(root):
        nonlocal arr

        if root.left != None:
            dfs(root.left)

        arr.append(root.value)

        if root.right != None:
            dfs(root.right)

    dfs(root)
    return arr

def convert_tree(T): # slaba zloznosc pamieciowa
    arr = sort_bts(T)
    root = Node()
    root.value = arr[0]
    
    for i in range(len(arr)):
        temp = Node()
        arr[i] = temp.value[arr[i]]

    i = 0
    while i < len(arr):
        if 2 * i + 1 < len(arr):
            arr[i].left = arr[2 * i + 1]
            arr[2 * i + 1].parent = arr[i]
            
        if 2 * i + 2 < len(arr):
            arr[i].right = arr[2 * i + 2]
            arr[2 * i + 1].parent = arr[i]
        i += 1

    return arr[0]





A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
A.left = B
A.right = C
B.left = D
B.right = E
E.left = F

A.value = 11
B.value = 3
C.value = 13
D.value = 2
E.value = 7
F.value = 5

