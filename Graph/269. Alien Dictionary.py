
def dfs(graph, source, visited, result):
    visited[source] = True  

    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, result)
    result.append(source)



def topological_sort(graph):
    result = []
    visited = [False] * len(graph)

    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, result)
    
    return result[::-1]




def alien_dictionary_brute():
    # we need to use a topological sort
    pass



graph = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]

print(topological_sort(graph))