        def relax(u, v, distance, parent):
            if distance[v[0]] > distance[u] + v[1]:
                distance[v[0]] = distance[u] + v[1]
                parent[v[0]] = u 
                return True
            return False
        

        def dijkstra_algorithm(graph, source):
            queue = PriorityQueue()
            queue.put((0, source))
            parent = [None] * len(graph)
            distance = [inf] * len(graph)
            visited = [False] * len(graph)
            distance[source] = 0
            while not queue.empty():
                dist, u = queue.get()
                for v in graph[u]:
                    if not visited[v[0]] and relax(u, v, distance, parent):
                        queue.put((dist + v[1], v[0]))
                visited[u] = True
            return parent, distance