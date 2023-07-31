class Solution2:
    def findRedundantDirectedConnection(self, edges):
        def create_graph(edges):
            no_vertices = 0
            for i in range(len(edges)):
                no_vertices = max(no_vertices, edges[i][0], edges[i][1])
            graph = [[] for _ in range(no_vertices)]
            undirected_graph = [[] for _ in range(no_vertices)]
            for i in range(len(edges)):
                graph[edges[i][0]-1].append(edges[i][1]-1)
                undirected_graph[edges[i][0]-1].append(edges[i][1]-1)
                undirected_graph[edges[i][1]-1].append(edges[i][0]-1)
            return graph, undirected_graph
        
        new_graph, undirected_graph = create_graph(edges)
        noways = [0] * len(new_graph)
        noways[0] = 1
        visited = [False] * len(new_graph)
        
        def dfs(node):
            visited[node] = True
            for i in new_graph[node]:
                noways[i] +=1
                if not visited[i]:
                    dfs(i)
        dfs(0)
        print(noways)
        redundant = []
        for i in range(len(noways)):
            if noways[i] > 1:
                redundant.append(i)
        redundant_edge = -1

        for i in range(len(edges)-1, -1, -1):
            if edges[i][1]-1 in redundant and len(undirected_graph[edges[i][0] - 1]) > 1:
                redundant_edge = edges[i]
                break
        return redundant_edge


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.rank = 0

def find(x):
    if x!=x.parent:
        x.parent = find(x.parent)
    return x.parent

def make_set(val):
    return Node(val)

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank +=1

class Solution:
    def findRedundantDirectedConnection(self, edges):
        no_vertices = 0
        for i in range(len(edges)):
            no_vertices = max(no_vertices, edges[i][0], edges[i][1])
        V = []

        for i in range(no_vertices):
            V.append(make_set(i))

        for i in range(len(edges)):
            u = edges[i][0]-1
            v = edges[i][1]-1
            if find(V[u]) != find(V[v]):
                union(V[u], V[v])
            else:
                return edges[i]

edges = [[2,1],[3,1],[4,2],[1,4]]
#sol = Solution()
#print(sol.findRedundantDirectedConnection(edges))