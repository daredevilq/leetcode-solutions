from queue import PriorityQueue
from math import inf
class Solution:
    def minCost(self, maxTime, edges, passingFees):
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
        
        no_verticies = 0
        for i in range(len(edges)):
            no_verticies = max(no_verticies, edges[i][0], edges[i][1])
        no_verticies += 1

        def make_graph(edges):
            graph = [[] for _ in range(no_verticies)]
            for u, v, w in edges:
                graph[u].append((v,w))
                graph[v].append((u,w))

            return graph
        
        new_graph = make_graph(edges)
        print(new_graph)
        distance, parent = dijkstra_algorithm(new_graph, 0)
        print(distance)

        if distance[no_verticies - 1] > maxTime:
            return -1
        
        cost = 0
        i = no_verticies - 1

        while i != 0:
            cost += passingFees[i]
            i = parent[i]
        cost += passingFees[0]

        return cost
    


sol = Solution()
maxTime = 30
edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
passingFees = [5,1,2,20,20,3]
print(sol.minCost(maxTime, edges, passingFees))
