class Solution:
    # we hava stock -> 1
    # we dont hace stock -> 0


    def dp(self, i, stock, prices, memo):
        if i == len(prices):
            return 0
        
        if (i, stock) in memo:
            return memo[(i, stock)]


        we_have_stock = 0
        we_dont_have_stock = 0

        if stock == 1:
            we_have_stock = max(self.dp(i+1, 0, prices, memo) + prices[i], self.dp(i+1, 1, prices, memo)) 
        else:
            we_dont_have_stock = max(self.dp(i+1, 1, prices, memo) - prices[i], self.dp(i+1, 0, prices, memo)) 

        max_profit = max(we_have_stock, we_dont_have_stock)

        memo[(i, stock)] = max_profit

        return max_profit

        

    def maxProfit(self, prices) -> int:
        memo = {}    
        return self.dp(0, 0, prices, memo)
    

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # dp[i][0] means the maximum profit we can get until day i with no stock in hand
        # dp[i][1] means the maximum profit we can get until day i with one stock in hand
        dp = [[0]*2 for _ in range(n+1)]
        
        # Base case initialization
        dp[0][0] = 0
        dp[0][1] = -float('inf')  # We can't have stock in hand on day 0

        for i in range(1, n+1):
            # If we don't have stock on day i, we could either not have stock on day i-1 or sell the stock on day i
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            # If we have stock on day i, we could either have stock on day i-1 or buy the stock on day i
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i-1])
        
        # The answer will be the maximum profit we can get without having stock on the last day
        return dp[n][0]

sol = Solution()
prices = [7,6,4,3,1]

print(sol.maxProfit(prices))