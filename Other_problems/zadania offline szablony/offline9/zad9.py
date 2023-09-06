from zad9testy import runtests

from queue import Queue
from math import inf


def bfs(graph, s, t, parent):
    queue = Queue()
    visited = [False] * len(graph)
    visited[s] = True
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                parent[v] = u
                queue.put(v)
    return visited[t]

 
def edmonds_karp_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow 
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow


def make_graph(edges ):
    V = 0

    for i in range(len(edges)):
        V = max(V, edges[i][0], edges[i][1])
    V += 1

    graph = [[0] * V for _ in range(V)] 

    for i in range(len(edges)):
        graph[edges[i][0]][edges[i][1]] = edges[i][2]

    return graph


def maxflow( G,s ):
    graph = make_graph(G)
    best1 = -1
    best2 = -1
    temp_graph = graph
    for i in range(len(graph)):
        if i != s:
            flow = edmonds_karp_algorithm(temp_graph, s, i)
            if flow>best1:
                best2 = best1
                best1 = flow
            elif flow>best2:
                best2 = flow
            temp_graph = graph
    return best1 + best2

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )