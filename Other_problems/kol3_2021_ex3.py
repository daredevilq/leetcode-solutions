from math import inf

def floyd_warshall(G):
    distances = [[inf] * len(G) for _ in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G)):
            if i == j:
                distances[i][j] = inf
            elif G[i][j] == 0:
                distances[i][j] = inf
            else:
                distances[i][j] = G[i][j]
            
    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                if i == j:
                    distances[i][j] = inf
                else:
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    

    return distances










def BlueAndGreen(T, K, D):
    dist = floyd_warshall(T)
    
    new_graph = [[0] * (len(T) + 2) for _ in range(len(T) + 2)]

    for i in range(len(T)):
        for j in range(len(T)):
            if i != j and inf > dist[i][j] >= D:
                new_graph[i][j] = 1
                new_graph[j][i] = 1


T = [
[0, 1, 1, 0, 1],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
]

BlueAndGreen(T,2,2)