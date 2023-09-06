from math import inf
# jedzie jacek i marian
# driver = 0 - jacek
# driver = 1 - marian
arr = []



def drivers(P, B):
    P = sorted(P)

    memo = [[[inf] * 4 for _ in range(2)] for _ in range(len(P) + 1)] # memo[i][driver][no_non_changes] = min changes to get to the end 
    changes = []

    def solve(i, driver, no_non_changes):
        nonlocal memo
        if i == len(P):
            return 0
        
        if no_non_changes > 3:
            return inf

        if memo[i][driver][no_non_changes] != inf:
            return memo[i][driver][no_non_changes]

        res1 = inf
        res2 = inf
        res3 = inf
        res4 = inf

        if P[i][1] == True:
            if driver == 0:
               new_driver = 1
            else:
                new_driver = 0

            res1 = 0 + solve(i+1, new_driver, 0)  # zmienamy sie 
            res2 = 0 + solve(i+1, driver, no_non_changes+1)

        else:
            if driver == 0:
                res3 = 0 + solve(i+1, driver, no_non_changes)
            else:  
                res4 = 1 + solve(i+1, driver, no_non_changes)

        res = min(res1, res2, res3, res4)
        memo[i][driver][no_non_changes] = res
        return res
    def reconstruct(i, driver, no_non_changes):
        nonlocal memo
        nonlocal changes
        if i == len(P):
            return

        res1 = inf
        res2 = inf
        res3 = inf
        res4 = inf
    


        if P[i][1] == True:
            if driver == 0:
               new_driver = 1
            else:
                new_driver = 0

            res1 = 0 + memo[i+1][new_driver][0]  # zmienamy sie
            res2 = 0 + memo[i+1][driver][no_non_changes+1]
        else:
            if driver == 0:
                res3 = 0 + memo[i+1][driver][no_non_changes]
            else:  
                res4 = 1 + memo[i+1][driver][no_non_changes]
        
        res = min(res1, res2, res3, res4)

        if res == res1:
            changes.append(P[i][0])
            reconstruct(i+1, new_driver, 0)
        elif res == res2:
            reconstruct(i+1, driver, no_non_changes+1)
        elif res == res3:
            reconstruct(i+1, driver, no_non_changes)
        else:
            reconstruct(i+1, driver, no_non_changes)

    ans = solve(0, 0, 0)
    print(ans)
    reconstruct(0, 0, 0)
    print(changes)

p = True
c = False
#      0      1      2      3      4      5       6       7       8       9      10     11     12      13     14      15      16      17    
P = [(1,c), (3,c), (4,c), (6,c), (8,c), (9,c), (11,c), (13,c), (16,c), (17,c), (2,p), (5,p), (7,p), (10,p), (12,p), (14,p), (15,p), (18,p)]
B = 20

drivers(P, B)


def solve_knapsack(P,W,max_w, i, act_weight, memo):
    if i == len(P):
        return 0
    if (i, act_weight) in memo:
        return memo[(i, act_weight)]
    
    res1 = 0
    res2 = 0

    if act_weight + W[i] <= max_w:
        res1 = P[i] + solve_knapsack(P,W,max_w, i+1, act_weight + W[i], memo)
    res2 = solve_knapsack(P,W,max_w, i+1, act_weight, memo)

    res = max(res1, res2)
    memo[(i, act_weight)] = res
    return res

def foo(P,W,max_w, i, act_weight, memo, path):
    test = []
    def solve_knapsack2(P,W,max_w, i, act_weight, memo):
        nonlocal test
        if i == len(P):
            return 0
        if memo[i][act_weight] != -1:
            return memo[i][act_weight]

        res1 = 0
        res2 = 0 

        if act_weight + W[i] <= max_w:
            res1 = P[i] + solve_knapsack2(P,W,max_w, i+1, act_weight + W[i], memo)
        res2 = solve_knapsack2(P,W,max_w, i+1, act_weight, memo)

        res = max(res1, res2)
        if res1 > res2: 
            test.append(i)
        memo[i][act_weight] = res
        return res
    return solve_knapsack2(P,W,max_w, i, act_weight, memo), test


def knapsack3(P, W, w_max):
    memo = {}
    items = [-1] * len(P)
    def sol(P, W, i, act_weight, memo):

        nonlocal items
        if i == -1:
            return 0
        if (i, act_weight) in memo:
            return memo[(i, act_weight)]
        res1 = 0
        res2 = 0

        if act_weight - W[i] >= 0:
            res1 = P[i] + sol(P, W, i-1, act_weight - W[i], memo)
        res2 = sol(P, W, i-1, act_weight, memo)

        if res1 > res2:
            items.append(i)
        res = max(res1, res2)
        
        memo[(i, act_weight)] = res
        return res

    ans = sol(P, W, len(P)-1, w_max, memo)
    print(ans)
    print(items)


def knapsack(P, W, max_w):
    memo = {}
    path = [-1] * len(P)

    memo2 = [[-1] * (max_w + 1) for _ in range(len(P))]
    ans = solve_knapsack(P,W,max_w, 0, 0, memo) 

    ans2, test = foo(P,W,max_w, 0, 0, memo2, path)
    for i in memo2:
        print(i)
    print(test)
    return ans2

########################

# interesting reconstruction

def KNAPSACK(P, W , max_w):
    memo = {}
    def solvek(i, capacity):
        nonlocal memo
        if i == len(P):
            return 0
        if (i, capacity) in memo:
            return memo[(i, capacity)]
        
        res1 = solvek(i+1, capacity) + 0

        res2 = 0

        if capacity - W[i] >= 0:
            res2 = solvek(i+1, capacity - W[i]) + P[i]
        
        res = max(res1, res2)
        memo[(i, capacity)] = res
        return res

    def reconstruct(i, capacity):
        nonlocal memo   
        if i == len(P):
            return 
        res1 = memo[(i+1, capacity)] # nie bioeremy
        res2 = 0
        if capacity - W[i] >= 0:
            res2 = memo[(i+1, capacity - W[i])] + P[i] # bierzemy

        if res1 > res2:
            reconstruct(i+1, capacity)
        else:
            print(i)
            reconstruct(i+1, capacity - W[i]) + P[i]
    
    solvek(0, max_w)
    print(memo)
    reconstruct(0, max_w)
    




def KNAPSACK2(P, W , max_w):

    memo = [[-1] * (max_w + 1) for _ in range(len(P) + 1)]
    def solvek2(i, capacity):
        nonlocal memo
        if i == len(P):
            return 0
        
        if memo[i][capacity] != -1:
            return memo[i][capacity]
        
        res1 = solvek2(i+1, capacity) + 0

        res2 = 0

        if capacity - W[i] >= 0:
            res2 = solvek2(i+1, capacity - W[i]) + P[i]
        
        res = max(res1, res2)
        memo[i][capacity] = res
        return res
    
    def reconstruct2(i, capacity):
        nonlocal memo   
        if i == len(P):
            return 
        res1 = memo[i + 1][capacity] # nie bioeremy
        res2 = 0
        if capacity - W[i] >= 0:
            res2 = memo[i + 1][capacity - W[i]] + P[i] # bierzemy

        if res1 > res2:
            reconstruct2(i+1, capacity)
        else:
            print(i)
            reconstruct2(i+1, capacity - W[i]) 
    
    solvek2(0, max_w)
    reconstruct2(0, max_w )


#P = [10, 8, 4, 5, 3, 7]
#W = [4, 5, 12, 9, 1, 13]
#max_W = 24
P = [10, 1,  20, 1, 40, 1, 30]
W = [5, 1,  5, 1, 5, 1, 5]
max_W = 20


#print(knapsack(P, W, max_W))
#knapsack3(P, W, max_W)

#KNAPSACK2(P, W, max_W)

