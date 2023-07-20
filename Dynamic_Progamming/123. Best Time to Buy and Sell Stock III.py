class Solution:
    def maxProfit(self, prices):
        def solve(i, buysell, cap, memo):  

            if i >= len(prices) or cap == 0:
                return 0
            
            if (i, buysell, cap) in memo:
                return memo[(i, buysell, cap)]              

            result1 = 0
            result2 = 0

            if buysell == 1: 
                result1 = max(-prices[i] + solve(i + 1, 0, cap, memo), 0 + solve(i+1, 1, cap, memo))
            else: 
                result2 = max(prices[i] + solve(i + 1, 1, cap - 1, memo), 0 + solve(i + 1, 0, cap, memo))

            result = max(result1 , result2)

            memo[(i, buysell, cap)] = result
            return result


        memo = {}
        ans = solve(0,1, 2,memo)
        return ans
    


sol = Solution()
prices = [3,3,5,0,0,3,1,4]
print(sol.maxProfit(prices))
