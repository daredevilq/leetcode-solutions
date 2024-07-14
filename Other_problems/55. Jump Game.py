class Solution:
    def canJump(self, nums) -> bool:
        arr = [False] * len(nums)
        arr[0] = True

        for i in range(len(nums)):
            if arr[i] == True:
                for j in range(nums[i]):
                    if i + j + 1 < len(nums):
                        arr[i + j + 1] = True
        return arr[-1]
    

class Solution:
    def canJump(self, nums) -> bool:
        target_index = len(nums) - 1

        for i in range(len(nums) -2, -1, -1):
            if target_index - i <= nums[i]:
                target_index = i 

        if target_index == 0:
            return True
        else: 
            return False 



nums = [3,2,1,0,4]

sol  = Solution()

print(sol.canJump(nums))