def solve(G,curr_city, visited, no_visited, prev_city, parents):

    if curr_city == 0 and prev_city != None:
        if no_visited == len(G):
            return True
        else:
            return False
        
    gate_side = None
    if curr_city != 0:
        if prev_city in G[curr_city][0]:
            gate_side = "north"
        else:
            gate_side = "south"
    print(curr_city, no_visited, prev_city, gate_side)
    res1 = False
    res2 = False
    res3 = False
    if gate_side == "north":
        for i in G[curr_city][1]:
            if visited[i] == False or i == 0:
                visited[i] = True
                no_visited += 1
                if solve(G,i,visited,no_visited, curr_city, parents):
                    if parents[i] == None:
                        parents[i] = curr_city
                    res1 = True
                visited[i] = False
                no_visited -= 1

    elif gate_side == "south":
        for i in G[curr_city][0]:
            if visited[i] == False or i == 0:
                visited[i] = True
                no_visited += 1
                if solve(G,i,visited, no_visited, curr_city, parents):
                    if parents[i] == None:
                        parents[i] = curr_city
                    res2 = True
                visited[i] = False
                no_visited -= 1
    else:       
        for i in G[curr_city][0]:
            if visited[i] == False or i == 0:
                visited[i] = True
                no_visited += 1
                if solve(G,i,visited,no_visited, curr_city, parents):
                    if parents[i] == None:
                        parents[i] = curr_city
                    res3 = True
                visited[i] = False
                no_visited -= 1

        for i in G[curr_city][1] or i == 0:
            if visited[i] == False:
                visited[i] = True
                no_visited += 1
                if solve(G,i,visited,no_visited, curr_city, parents):
                    if parents[i] == None:
                        parents[i] = curr_city
                    res3 = True
                visited[i] = False
                no_visited -= 1
                
    return res1 or res2 or res3
    
def droga( G ):
    parents = [None] * len(G)
    visited = [False] * len(G)
    no_visited = 0
    prev_city = None
    visited[0] = True
    res =  solve(G,0,visited,no_visited, prev_city, parents)
    if res:
        return parents

G2 = [ ([1],[2,3,4]),
([0],[2,5,6]),
([1,5,6],[0,3,4]),
([0,2,4],[5,7,8]),
([0,2,3],[6,7,9]),
([1,2,6],[3,7,8]),
([1,2,5],[4,7,9]),
([4,6,9],[3,5,8]),
([3,5,7],[9]),
([4,6,7],[8]) ]

G =  [([1], [3]), ([2], [0]), ([3], [1]), ([0], [2])]

print(droga(G))