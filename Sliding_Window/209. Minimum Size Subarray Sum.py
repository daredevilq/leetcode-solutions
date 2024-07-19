from math import inf

class Solution:
    def minSubArrayLen(self, target, nums):
        min_no_values = float('inf')
        sum = 0

        i = 0
        j = 0

        while i < len(nums):
            sum += nums[i]
            i+=1
            while sum >= target:
                min_no_values = min(i - j, min_no_values)
                sum -= nums[j]
                j+=1
                    

        if min_no_values == float('inf'):
            return 0 
        
        return min_no_values
    


sol = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(sol.minSubArrayLen(target, nums))