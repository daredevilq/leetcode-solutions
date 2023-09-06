from math import inf

def common_digit(a, b):
    da = [False for _ in range(10)]
    db = [False for _ in range(10)]

    if a > b:
        temp = a
    else:
        temp = b

    while temp > 0:
        if a > 0:
            da[a % 10] = True
            a //= 10
        if b > 0:
            db[b % 10] = True
            b //= 10

        temp //= 10
    for i in range(10):
        if da[i] and db[i]:
            return True
    return False


def solve(T):
    dp = [inf for _ in range(len(T))]
    dp [0] = 0
    
    for i in range(len(T)):
        for j in range(1,len(T)):
            if i != j:
                if common_digit(T[i], T[j]):
                    #print(i,j)
                    dp[j] = min(dp[j], dp[i] + abs(T[i] - T[j]))
    print(dp)
    return dp[-1]

    


def dynamic(T):
    T.sort()
    print(T)
    ans = solve(T)
    print(common_digit(123, 246))
    if ans == inf:
        return -1
    return ans


T2 = [123,890,688,587,257,246]
T = [587,990,257,246,668,132]

print(dynamic(T))