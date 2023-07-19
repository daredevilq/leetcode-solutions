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
        result = recursion(0,memo)
        print(memo)
        return result