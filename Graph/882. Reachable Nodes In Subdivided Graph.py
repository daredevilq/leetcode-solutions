from queue import Queue
from math import inf
class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        
        added = n
        new_list_of_edges = []
        for i in range(len(edges)):
            for j in range(edges[i][2]+1):
                if j == 0:
                    new_list_of_edges.append([edges[i][0], added])
                elif j == edges[i][2]:
                    new_list_of_edges.append([added, edges[i][1]])
                else:
                    new_list_of_edges.append([added, added+1])
                    added += 1
            added += 1
        graph = [[] for _ in range(added)]

        for i in range(len(new_list_of_edges)):
            graph[new_list_of_edges[i][0]].append(new_list_of_edges[i][1])
            graph[new_list_of_edges[i][1]].append(new_list_of_edges[i][0])

        visited = [False for _ in range(len(graph))]
        distance = [inf for _ in range(len(graph))]        
        parent = [-1 for _ in range(len(graph))]
        distance[0] = 0
        queue = Queue()
        queue.put(0)
        
        while not queue.empty():
            v = queue.get()
            for u in graph[v]:
                if not visited[u]:
                    visited[u] = True
                    distance[u] = distance[v] + 1
                    queue.put(u)
        distance[0] = 0
        
        counter = 0
        for i in range(len(distance)):
            if distance[i] <= maxMoves:
                counter += 1
        return counter


edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]]
maxMoves = 17
n = 5
sol = Solution()
print(sol.reachableNodes(edges, maxMoves, n))
