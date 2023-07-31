
class Solution2: # doesnt work xd
    def minTrioDegree(self, n,  edges):
        def find_cycles(graph, parents):
            visited = [False] * len(graph)
            cycles=[]
            visited_edges = 0
            def dfs(v):
                nonlocal visited_edges
                visited[v] = True
                visited_edges += 1
                for u in graph[v]:
                    if not visited[u]:
                        parents[u] = v
                        dfs(u)
                    elif visited[u] and parents[v] != u:
                        cycles.append([v,u])
            i = 0
            while visited_edges < len(graph):
                if not visited[i]:
                    dfs(i)
                i += 1
            return cycles

        def make_graph(edges):
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u-1].append(v-1)
                graph[v-1].append(u-1)
            return graph
        
        graph = make_graph(edges)
        #print(graph)
        parents = [None] * len(graph)
        cycles_ends = find_cycles(graph, parents)
        cycles = []
        for i in range(len(cycles_ends)):
            u, v = cycles_ends[i]
            cycle = [u]
            while u != v:
                u = parents[u]
                if u == None:
                    break
                cycle.append(u)
            if len(cycle) == 3:
                cycles.append(cycle)

        print(cycles_ends)
        print(parents)
        best_degree = 10 ** 5

        for i in range(len(cycles)):
            degree = 0
            for v in cycles[i]:
                for u in graph[v]:
                    if u not in cycles[i]:
                        degree += 1
            best_degree = min(best_degree, degree)
        
        if best_degree == 10 ** 5:
            return -1
        return best_degree





class Solution:
    def minTrioDegree(self, n, edges):
        def make_graph(edges):
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u-1].append(v-1)
                graph[v-1].append(u-1)
            return graph

        graph = make_graph(edges)
        print(graph)
        cycles = []
        for i in range(len(graph)):
            for j in graph[i]:
                for k in graph[j]:
                    for h in graph[k]:
                        if h == i:
                            cycles.append([i, j, k])
        print(cycles)
        best_degree = 10 ** 5
        for i in range(len(cycles)):
            degree = 0
            for v in cycles[i]:
                degree += len(graph[v]) - 2
            best_degree = min(best_degree, degree)
        if best_degree == 10 ** 5:
            return -1
        return best_degree



n = 6
#edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
edges = [[6,5],[4,3],[5,1],[1,4],[2,3],[4,5],[2,6],[1,3]]
#sol = Solution2()
#print(sol.minTrioDegree(n, edges))
sol = Solution()
print(sol.minTrioDegree(n, edges))