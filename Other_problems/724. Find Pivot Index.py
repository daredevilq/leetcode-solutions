class Solution:
    def pivotIndex(self, nums) -> int:
        
        if(len(nums)) == 0:
            return 0
        
        left_sum = [0]*len(nums)
        right_sum = [0]*len(nums)

        left_sum[0] = nums[0]
        right_sum[len(nums) - 1] = nums[len(nums) - 1]
        n = len(nums)
        for i in range(1, len(nums)):
            left_sum[i] = left_sum[i-1] + nums[i]
            right_sum[n - i - 1] = right_sum[n - i] + nums[n - i - 1]

        for i in range(len(nums)):
            if left_sum[i] - nums[i] == right_sum[i] - nums[i]:
                return i 


        return -1

sol = Solution()
arr = [1,2,3,4,5,6,7,8,9,10]
print(sol.pivotIndex(arr))