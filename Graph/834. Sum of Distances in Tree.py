class Solution:
    def sumOfDistancesInTree(self, n, edges):
        no_vertices = 0
        def make_graph(edges):
            nonlocal no_vertices
            for i in range(len(edges)):
                no_vertices = max(no_vertices, edges[i][0], edges[i][1])
            no_vertices += 1

            graph = [[] for _ in range(no_vertices)]

            for i in range(len(edges)):
                graph[edges[i][0]].append(edges[i][1])
                graph[edges[i][1]].append(edges[i][0])
            
            return graph

        graph = make_graph(edges)
        visited = [False] * no_vertices

        def dfs(graph, node, curr_distance, distance):
            distance[node] = curr_distance
            visited[node] = True
            for u in graph[node]:
                if not visited[u]:
                    dfs(graph, u, curr_distance + 1, distance)
        
        answer = [0] * no_vertices
        for i in range(no_vertices):
            distance = [0] * no_vertices
            visited = [False] * no_vertices
            dfs(graph, i, 0, distance)
            answer[i] = sum(distance)
        
        return answer
    



sol = Solution()    
n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
print(sol.sumOfDistancesInTree(n, edges))
