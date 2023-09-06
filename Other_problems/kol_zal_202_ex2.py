from queue import Queue
def make_adj_graph(matrix):
    graph = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                graph[i].append(j)
    return graph
      
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


def bfs(graph, source, curr_art_point, visited):
    queue = Queue()
    queue.put(source)
    visited[source] = True
    v_counter = 1
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v] and v != curr_art_point:
                visited[v] = True
                queue.put(v)
                v_counter += 1
    return v_counter


def breaking(G):

    graph = make_adj_graph(G)
    art_points = find_articulation_points(graph)
    if art_points == []:
        return None
    
    parts = [-1] * len(art_points)
    #print("1")
    for i in range(len(art_points)):
        #print("2")
        visited = [False] * len(graph)
        v_counter = 0
        current_v = 0
        counter = 0
        while v_counter < len(graph) - 1:
            #print("3")
            if current_v != art_points[i]:
                #print("4")
                v_counter += bfs(graph, current_v, art_points[i], visited)
                #print("5")
                counter += 1
            current_v += 1
        parts[i] = counter
    
    max_indx = -1
    max_val = -1
    for i in range(len(parts)):
        if parts[i] > max_val:
            max_val = parts[i]
            max_indx = i
    return art_points[max_indx]



G = [[0, 1, 0],
     [1, 0, 1],
     [0, 1, 0]]
M4 = [[0, 1, 1, 1, 0, 0, 0],
      [1, 0, 0, 0, 1, 0, 0],
      [1, 0, 0, 0, 0, 1, 0],
      [1, 0, 0, 0, 0, 0, 1],
      [0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0]]

#graph = make_adj_graph(G)
print(breaking(M4))

