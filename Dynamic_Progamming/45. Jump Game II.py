class Solution:
    def jump(self, nums):
        inf = float("inf")
        def recursion(indx,memo):
            if indx == len(nums) - 1:
                return 0
            if indx >= len(nums):
                return inf

            if indx in memo:
                return memo[indx]

            res = inf
            if nums[indx] != 0:
                for i in range(1,nums[indx] + 1):
                    res = min(res, recursion(indx + i,memo)) + 1

            memo[indx] = res
            return res
        
        memo = {}
        #result = recursion(0,memo)

        
        dp = [inf]*len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i + j <len(nums):
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        
        
        return dp[-1]
    
    


sol = Solution()
nums = [2,3,1,1,4]
print(sol.jump(nums))