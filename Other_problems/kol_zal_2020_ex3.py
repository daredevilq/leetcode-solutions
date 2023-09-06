from math import inf

def tank(V, i, act_fuel, q):
    act_fuel += V[i]
    return min(act_fuel, q)

def solve(T, V, q, l, i, act_fuel, memo):
    
    if (i, act_fuel) in memo:
        (result, flagg) = memo[(i, act_fuel)]
        return result
    
    if act_fuel < 0:
        return inf
    
    if i == len(T) - 1:
        if act_fuel >= l - T[i]:
            return 0
        else:
            new_fuel = tank(V, i, act_fuel, q)
            if new_fuel >= l - T[i]:
                return 1
            else:
                return inf
    
            
    res1 = inf
    res2 = inf
    
    res1 = solve(T, V, q, l, i+1, act_fuel - (T[i + 1] - T[i]), memo) 
    res2 = 1 + solve(T, V, q, l, i+1, tank(V, i,act_fuel,q) - (T[i + 1] - T[i]), memo)
    flag = False

    if res2<res1:
        flag = True

    res = min(res1, res2)
    memo[(i, act_fuel)] = (res,flag)
    return res



####### bez uzycia memoizacji rtylko z tablica
def solve22(T, V, q, l, i, act_fuel, memo):
    def solve2(T, V, q, l, i, act_fuel, memo):

        if memo[i][act_fuel] != -1:
            (res, flag) = memo[i][act_fuel]
            return res
        
        if act_fuel < 0:
            return inf
        
        if i == len(T) - 1:
            if act_fuel >= l - T[i]:
                return 0
            else:
                new_fuel = tank(V, i, act_fuel, q)
                if new_fuel >= l - T[i]:
                    return 1
                else:
                    return inf
        
                
        res1 = inf
        res2 = inf
        
        res1 = solve2(T, V, q, l, i+1, act_fuel - (T[i + 1] - T[i]), memo) 
        res2 = 1 + solve2(T, V, q, l, i+1, tank(V, i,act_fuel,q) - (T[i + 1] - T[i]), memo)
        flag = False

        if res2<res1:
            flag = True

        res = min(res1, res2)
        memo[i][act_fuel] = (res, flag)
        return res
    
    ans = solve2(T, V, q, l, i, act_fuel, memo)
    return ans


def iamlate2(T, V, q, l):
    memo = {}
    arr = [[-1] * (q + 1) for _ in range(len(T) + 1)]
    res1 = solve(T, V, q, l, 0, q, memo) + 1
    res2 = solve22(T, V, q, l, 0, q, arr) + 1
    print(memo)
    print(res1, res2)
    for i in arr:
        print(i)
    


def prepare_stations(T, V, l):
    n = len(T)
    
    i = n - 1
    while i >= 0 and T[i] >= l:
        i -= 1
        
    T = T[:i + 1]
    V = V[:i + 1]
    T.append(l)
    V.append(0)
    
    return T, V


def iamlate(T, V, q, l):
    if T[0] != 0:
        []
    n = len(T)
    T, V = prepare_stations(T, V, l)
    F = [[inf] * (q + 1) for _ in range(n)]
    P = [[None] * (q + 1) for _ in range(n)]

    F[0][0] = 0

    for i in range(n - 1):
        for fuel in range(q + 1):
            if F[i][fuel] == inf:
                continue
            
            new_fuel = min(q, fuel + V[i])

            j = i + 1

            while j < n:
                distance = T[j] - T[i]
                remaining = new_fuel - distance
                if remaining < 0:
                    break
                
                if F[j][remaining] > F[i][fuel] + 1:
                    F[j][remaining] = F[i][fuel] + 1
                    P[j][remaining] = (i, fuel)
                j +=1
    
    for i in F:
        print(i)



T =  [0, 1, 2]
V =  [2, 1, 5]
q =  2
l =  4

iamlate(T, V, q, l)