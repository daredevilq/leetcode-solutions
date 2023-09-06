from math import inf

#############################################################################################################
                                        # BRIDGES IN A GRAPH



def bridges(graph):
    visited = [False] * len(graph)
    time_visit = [0] * len(graph)
    low = [inf] * len(graph)
    parent = [None] * len(graph)
    time = 0
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, parent, time_visit, time, low)
    for i in range(len(graph)):
        if time_visit[i] == low[i] and parent[i] is not None:
            print(parent[i], i)

 
def dfs(graph, source, visited, parent, time_visit, time, low):
    visited[source] = True
    time_visit[source] = time
    time += 1
    low[source] = time_visit[source]
    for v in graph[source]:
        if not visited[v]: 
            parent[v] = source
            dfs(graph, v, visited, parent, time_visit, time, low)
            low[source] = min(low[source], low[v])
        if parent[source] != v:
            low[source] = min(low[source], time_visit[v])


    

graph = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2], [3, 6], [3, 5, 7], [6]]
#print(bridges(graph))

#############################################################################################################
                                        # ARTICULATION POINTS IN A GRAPH

def find_articulation_points(G):
    n = len(G)
    low    = [0] * n
    times  = [0] * n
    is_art = [False] * n
    time   = 0
    
    def dfs(root, u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time
        out_deg = 0
        
        for v in G[u]:
            if v == parent: continue
            if not times[v]:
                out_deg += dfs(root, v, u) + u == root
                low[u] = min(low[u], low[v])
                if times[u] <= low[v]:
                    is_art[u] = True
            else:
                low[u] = min(low[u], times[v])
        
        return out_deg
                
    # Check all possible starting vertices as a graph doesn't have to be consistent
    for u in range(n):
        if not times[u]:
            is_art[u] = dfs(u, u, -1) > 1

    return [u for u in range(n) if is_art[u]]



graph = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2], [3, 6], [3, 5, 7], [6]]
#print(find_articulation_points(graph))

from queue import Queue

#############################################################################################################
                                    # BFS O(V+E) - Breadth First Search


def bfs(graph, source):
    queue = Queue()
    queue.put(source)
    visited = [False] * len(graph)
    visited[source] = True
    while not queue.empty():
        queue.get()
        for v in graph[source]:
            if not visited[v]:
                queue.put(v)
                visited[v] = True   



#############################################################################################################
                                # DFS O(V+E) - Depth First Search


def dfs(graph, source):
    visited = [False] * len(graph)
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v)



#############################################################################################################
                                # Topology sort O(V+E) dla DAG'u


def dfs(graph, source, visited, resu):
    visited[source] = True

    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, resu)
    resu.insert(0, source) # dopisujemy na poczatek listy

def topology_sort(graph):
    visited = [False] * len(graph)
    stack = []

    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, stack)
    return stack



#############################################################################################################
                            # detect cycle

def dfs(graph, source, visited, parent):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            parent[v] = source
            return dfs(graph, v, visited, parent)
        elif visited[v] and parent[source] != v:
            return True
    return False


def detect_cycle(graph):
    source = 0
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    return dfs(graph, source, visited, parent)






#############################################################################################################
                # Tree diamater - the longest path between two vertices in a tree


def dfs(graph, source, visited, distances):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            distances[v] = distances[source] + 1
            dfs(graph, v, visited, distances)



def tree_diameter(graph):
    distances = [0] * len(graph)
    visited = [False] * len(graph)

    dfs(graph, 0, visited, distances)
    max_v = distances.index(max(distances))

    distances = [0] * len(graph)
    visited = [False] * len(graph)

    dfs(graph, max_v, visited, distances)
    return max(distances), distances.index(max(distances))






#############################################################################################################
                    # strongly connected components 
                    #O(V+E) 


stack = [4,1, 3,5]

print(stack.pop())
#############################################################################################################
            # Bellman-Ford algorithm for finding the shortest paths from source vertex to all other vertices in graph
            #O(V*E)
from math import inf

def bellman_ford(graph, soruce):
    V = 0
    for i in range(len(graph)):
        V = max(V, graph[i][0], graph[i][1])
    
    distance = [inf] * (V + 1)
    parent = [None] * (V + 1)
    distance[soruce] = 0

    for i in range(V - 1):
        for j in range(len(graph)):
            if distance[graph[j][1]] > distance[graph[j][0]] + graph[j][2]:
                distance[graph[j][1]] = distance[graph[j][0]] + graph[j][2]
                parent[graph[j][1]] = graph[j][0]
    
    for i in range(len(graph)):
        if distance[graph[i][1]] > distance[graph[i][0]] + graph[i][2]:
            return False, "jest ujemny cykl"
    
    return True, distance, parent




#############################################################################################################
            # floyd warshall algorithm for finding the shortest paths between every pair of vertices in a given
            # O(n^3)

def floyd_warshall(graph):
    distances = [[inf] * len(graph) for _ in range(len(graph))]
    parent = [[None] * len(graph) for _ in range(len(graph))]

    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                distances[i][j] = 0
            elif graph[i][j] != -1:
                distances[i][j] = graph[i][j]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != -1:
                parent[i][j] = i
    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    parent[j][k] = parent[i][k]




#############################################################################################################
            # Ford Fulkerson algorithm for finding the maximum flow in a flow network
            # O(E*V^2)

            