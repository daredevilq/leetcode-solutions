from functools import *

class Solution2: #brute  
    def countDigitOne(self, n: int) -> int:
        counter = 0
        dp = [-1] * (n + 1)
        for i in range(1, n + 1):
            while i != 0:
                temp = i%10
                if temp == 1:
                    counter +=1
                i//=10
            
        return counter
    
class Solution3: # dobre rozwiazanei tylko ze python ma okolo 900 depth recursion
    def countDigitOne(self, n: int) -> int:

        def solve(n, memo):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]

            temp = n
            counter = 0
            while temp != 0:
                if temp%10 == 1:
                    counter+=1
                temp//=10
            
            counter += solve(n - 1, memo)
            memo[n] = counter
            return counter
    
        return solve(n,{})


class Solution:
    def countDigitOne(self, n: int) -> int:
        @cache
        def dfs(pos, cnt, limit):
            if pos <= 0:
                return cnt
            up = a[pos] if limit else 9
            ans = 0
            for i in range(up + 1):
                ans += dfs(pos - 1, cnt + (i == 1), limit and i == up)
            return ans

        a = [0] * 12
        l = 1
        while n:
            a[l] = n % 10
            n //= 10
            l += 1
        return dfs(l, 0, True)
    
sol = Solution()
sol3 = Solution3()
sol2 = Solution2()
print(sol3.countDigitOne(824))
print(sol2.countDigitOne(824))
print(sol.countDigitOne(8241))