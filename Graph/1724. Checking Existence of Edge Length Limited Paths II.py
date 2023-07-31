from math import inf

class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self  # wskazuje na samego siebie


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

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
            y.rank += 1


def make_set(v):
    return Node(v)




def kruskal(edges, no_vertices):
    edges.sort(key=lambda x: x[2])
    MST = []
    V = []
    for i in range(no_vertices):
        V.append(make_set(i))
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        if find(V[u]) != find(V[v]):
            MST.append(edges[i])
            union(V[u], V[v])
    return MST


def dfs(graph, start):
    distance = [inf] * len(graph)
    distance[start] = 0
    visited = [False] * len(graph)
    def dfs_visit(u, cost):
        distance[u] = cost

        for v, w in graph[u]:
            if not visited[v]:
                visited[v] = True
                dfs_visit(v, cost + w)
    return distance

def DistanceLimitedPathsExist(no_edges, edges):
    mst_edges = kruskal(edges, no_edges)
    new_graph = [[] for _ in range(no_edges)]

    for edge in mst_edges:
        new_graph[edge[0]].append((edge[1], edge[2]))
        new_graph[edge[1]].append((edge[0], edge[2]))

    ##### 
