def tasks(T):

    before_tasks = [[] for _ in range(len(T))]
    how_many = [0 for _ in range(len(T))]
    for i in range(len(T)):
        counter = 0
        for j in range(len(T)):
            if T[j][i] == 1:
                before_tasks[i].append(j)
                counter += 1
        how_many[i] = (counter,i)

    how_many.sort()
    ans = []
    i = 0
    for i in how_many:
        ans.append(i[1])
    
    return ans




T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ]

print(tasks(T))