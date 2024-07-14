class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 0
        
        for i in range(len(nums)):
            if k < 2 or nums[k - 2] != nums[i]:
                nums[k] = nums[i]
                k+=1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1
        return k
