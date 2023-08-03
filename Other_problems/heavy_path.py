from math import inf

class Node:
    def __init__(self):
        self.children = 0 # liczba dzieci wezla
        self.child = [] # lista par dziecko waga
        self.number = None


def make_graph(root):
    current_node = 0
    def dfs(node):
        nonlocal current_node

        node.number = current_node
        current_node += 1

        for u in node.child:
            dfs(u[0])
        
    dfs(root)

    graph = [[] for _ in range(current_node)]

    def dfs2(node):

        for u in node.child:
            graph[node.number].append((u[0].number, u[1]))
            graph[u[0].number].append((node.number, u[1]))
            dfs2(u[0])
    dfs2(root)
    return graph


def maximum_path(root, memo):
    if root.children == 0:
        return 0
    
    if root in memo:
        return memo[root]

    res = -inf
    for u in root.child:
        res = max(res, maximum_path(u[0], memo) + u[1])

    memo[root] = res
    return res

def heay_path(root):
    memo = {}
    answer = -inf
    def dfs(root):
        nonlocal answer
        nonlocal memo

        answer = max(answer, maximum_path(root, memo))

        for u in root.child:
            dfs(u[0])
    dfs(root)
    return answer


A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
A.children = 2
B.children = 2
B.child = [ (D,15), (E,11) ]
A.child = [ (B,5), (C,-1) ]


print(heay_path(A))