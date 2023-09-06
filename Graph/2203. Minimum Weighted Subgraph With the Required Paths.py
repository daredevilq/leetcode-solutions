from math import inf
from queue import PriorityQueue 

# alogrytm wymaga kilku zmian zeby przechodzil wszsytkie testty ale mi sie nie chce tego robic

class Solution:
    def make_graph( n, edges):
        graph = [[] for _ in range(n)]

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], edges[i][2]))

        return graph
    

    def dijkstra(graph, src):
        distances = [inf for _ in range(len(graph))]
        parents = [None for _ in range(len(graph))]
        distances[src] = 0
        visited = [False] * len(graph)
        queue = PriorityQueue()
        queue.put((0, src))

        while not queue.empty():
            dist, u = queue.get()

            for v in graph[u]:
                if not visited[v[0]]:
                    if distances[v[0]] > distances[u] + v[1]:
                        distances[v[0]] = distances[u] + v[1]
                        parents[v[0]] = u
                        queue.put((distances[v[0]], v[0]))
            visited[u] = True
        
        return distances, parents

    def minimumWeight(self, n, edges, src1, src2, dest):
        graph = Solution.make_graph(n, edges)
        print(graph)
        distances1, parents1 = Solution.dijkstra(graph, src1)   
        distances2, parents2 = Solution.dijkstra(graph, src2)
        
        print(distances1, parents1)
        print(distances2, parents2)

        if distances1[dest] == inf or distances2[dest] == inf:
            return -1
        
    

        summ = distances1[dest]
        act_node = dest
        merege_node  = None

        path2 = []
        path1 = [False] * len(graph)
        
        
        while act_node != src2:
            if act_node != dest:
                path2.append(act_node)
            act_node = parents2[act_node]

        path2.reverse()
        for i in range(len(parents1)):
            if parents1[i] != None:
                path1[parents1[i]] = True
                
        merge_node = None
        i = 0
        while merege_node != None:
            if path1[path2[i]]:
                merge_node = path2[i]
                break
            i += 1
        print(merge_node)
        if merge_node != None:
            summ += distances2[merge_node]
        else:
            summ += distances2[dest]
        

        summ = min(summ, distances1[src2] + distances2[dest], distances2[src1] + distances1[dest])

        return summ



n = 6
edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
src1 = 0
src2 = 1
dest = 5

s = Solution()
print(s.minimumWeight(n, edges, src1, src2, dest))