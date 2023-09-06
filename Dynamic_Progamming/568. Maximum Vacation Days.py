from math import inf



def solve(flights, days, current_city, current_week, memo):

    if current_week >= len(days[0]):
        return 0
    
    if (current_city, current_week) in memo:
        return memo[(current_city, current_week)]

    res1 = -inf
    res2 = -inf
    
    # we stay at current city
    res1 = days[current_city][current_week%7] + solve(flights, days, current_city, current_week + 1, memo)

    # we go to another city
    for i in range(len(flights)):
        if flights[current_city][i] == 1:
            res2 = max(res2, days[i][current_week] + solve(flights, days, i, current_week + 1, memo))

    res = max(res1, res2)
    memo[(current_city, current_week)] = res
    return res



def vacations_days(flights, days):
    memo = {}
    answer = solve(flights, days, 0, 0, memo)
    return answer


def vacations_days_2(flights, days):
    dp = [[0] * (len(days[0])) for _ in range(len(days))]

    for i in range(len(days)):
        dp[i][0] = days[i][0] 

    dp[0][0] = days[0][0]
    for i in range(1, len(days[0])):
        if flights[0][i] == 1:
            dp[0][i] = days[0][i] + dp[0][i - 1]
        else:
            dp[0][i] =  dp[0][i - 1]


    for i in range(len(days)):
        for j in range(len(days[0])):
            pass
        #to be done 



flights = [[0,1,1],
           [1,0,1],
           [1,1,0]]
days = [[1,3,1],
        [6,0,3],
        [3,3,3]]

print(vacations_days(flights, days))
vacations_days_2(flights, days)