from queue import PriorityQueue
from math import inf

def make_graph(G):
    no_verticies = 0

    for i in range(len(G)):
        no_verticies = max(no_verticies, G[i][0], G[i][1])
    no_verticies += 1

    graph = [[] for _ in range(no_verticies)]

    for i in range(len(G)):
        graph[G[i][0]].append((G[i][1], G[i][2]))
        graph[G[i][1]].append((G[i][0], G[i][2]))

    return graph




def dijkstra(graph, start, W, L):
    queue = PriorityQueue()
    visited = [False for _ in range(len(graph))]
    distance = [inf for _ in range(len(graph))]
    sum_distance = 0
    distance[start] = 0 
    queue.put((0, start, 0))
    iterator = 1
    word = W[0]
    last = -1
    while not queue.empty() and iterator < len(W):
        dist, u, l = queue.get()
        #print(u, L[u])
        for (v, w) in graph[u]:
            if not visited[v] and W[l + 1] == L[v]:
                print("here")
                last = v
                new_dist = distance[u] + w
                if new_dist < distance[v]:
                    distance[v] = new_dist
                    queue.put((new_dist, v, iterator))
                    print(L[u], u,"->",L[v], v)

        iterator += 1
        visited[u] = True
 
    if L[last] != W[-1]:
        return inf
    
    return distance[last]

def letters(E, L, W):
    graph = make_graph(E)
    best_result = inf
    start_indexes =[]

    for i in range(len(L)):
        if L[i] == W[0]:
            start_indexes.append(i)
    for i in start_indexes:
        best_result = min(best_result, dijkstra(graph, i, W, L))
        #print("asdada")
    if best_result == inf:
        return -1
    return best_result


L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
W = "kto"

print(letters(E, L, W))