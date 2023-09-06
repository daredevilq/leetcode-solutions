def solve(G,curr_city, visited, no_visited, prev_city):
    if no_visited == len(G):
        if curr_city == 0:
            return True
        else:
            print("dasda")
            return False
        
    gate_side = None
    if curr_city != 0:
        if curr_city in G[prev_city][0]:
            gate_side = "north"
        else:
            gate_side = "south"

    res1 = False
    res2 = False
    res3 = False
    if gate_side == "north":
        for i in G[curr_city][1]:
            if visited[i] == False:
                visited[i] = True
                no_visited += 1
                if solve(G,i,visited,no_visited, curr_city):
                    res1 = True

    elif gate_side == "south":
        for i in G[curr_city][1]:
            if visited[i] == False:
                visited[i] = True
                no_visited += 1
                if solve(G,i,visited, no_visited, curr_city):
                    res2 = True
    else:
        for i in G[curr_city][0]:
            if visited[i] == False:
                visited[i] = True
                no_visited += 1
                if solve(G,i,visited,no_visited, curr_city):
                    res3 = True
        for i in G[curr_city][1]:
            if visited[i] == False:
                visited[i] = True
                no_visited += 1
                if solve(G,i,visited,no_visited, curr_city):
                    res3 = True
                    
    return res1 or res2 or res3
    
def droga( G ):
    visited = [False] * len(G)
    no_visited = 0
    prev_city = None
    return solve(G,0,visited,no_visited, prev_city)