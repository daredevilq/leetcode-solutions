from math import inf

class Solution:
    def maxSubArray(self, nums):
        max_sum = -inf
        arr = [0]*len(nums)
        arr[0] = nums[0]
        for i in range(1, len(nums)):
            arr[i] = arr[i-1] + nums[i]

        start = -1
        end = -1

        for i in range(len(nums)):
             for j in range(i, len(nums)):
                if i == j:
                    if max_sum < arr[i]:
                        max_sum = arr[i]
                        start = i
                        end = i
                else:
                    if max_sum < arr[j] - arr[i]:
                        max_sum = arr[j] - arr[i]
                        start = i
                        end = j
        return max_sum
            
    
class Solution:
    def maxSubArray(self, nums):
        result = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            result = max(current_sum, result)
        
        return result
    



arr = [-2,1,-3,4,-1,2,1,-5,4]

sol = Solution()

print(sol.maxSubArray(arr))
                

        