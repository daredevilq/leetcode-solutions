from queue import PriorityQueue
from math import inf


def relax(graph, u, v, distance, parent):
    if distance[u] > distance[v] + graph[v][u]:
        distance[u] = distance[v] + graph[v][u]
        parent[u] = v
        return True
    return False
 

def jak_dojade(G, P, d, a, b):
    queue = PriorityQueue()
    distance = [inf] * len(G)
    visited = [False] * len(G)
    actual_fuel = d   
    queue.put((0, actual_fuel, a))
    distance[a] = 0
    parent = [None]*len(G)
    gas_stations = [False] * len(G)

    for i in P:
        gas_stations[i] = True

    while not queue.empty():
        dist, actual_fuel, v = queue.get()

        for u in range(len(G[v])):
            if G[v][u] != -1 and not visited[u]:
                if actual_fuel >= G[v][u]:
                    if relax(G, u, v, distance, parent):
                        actual_fuel -= G[v][u]
                        if gas_stations[u]:
                            actual_fuel = d 
                        queue.put((distance[u], actual_fuel, u))
        visited[v] = True

    print(parent)
    # mamy parent i teraz pozostaje tylko rekonstrukcja sciezki ktorej mi sei nie chce robic


G = [[-1, 6,-1, 5, 2],
    [-1,-1, 1, 2,-1],
    [-1,-1,-1,-1,-1],
    [-1,-1, 4,-1,-1],
    [-1,-1, 8,-1,-1]]

P = [0,1,3]

jak_dojade(G,P,5,0,2)