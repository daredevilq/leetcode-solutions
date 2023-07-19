# locked
from math import inf

def paint_house2(T):
    dp = [[inf] * len(T[0]) for _ in range(len(T))]
    
    last_colour = -1
    dp[0][0] = T[0][0]
    for i in range(1,len(T[0])):
        dp[0][i] = min(dp[0][i - 1], T[0][i])


    for i in range(1,len(T)):
        pass    




def paint_house2_rec(T):


    def solve(i,k,memo):
        if i >= len(T):
            return 0
        
        if (i,k) in memo:
            return memo[(i,k)]

        result = inf
        for j in range(len(T[0])):
            if j != k: 
                result = min(result, solve(i + 1,j,memo) + T[i][j])
        
        memo[(i,k)] = result
        return result
    memo = {}
    return solve(0,0,memo)


T= [[1,5,3],[2,9,4]]
print(paint_house2_rec(T))

