class Solution:
    def longestConsecutive(self, nums):
        chain = {} # (val, next_val)

        for i in range(len(nums)):
            response = chain.get(nums[i])
            prev = chain.get(nums[i] - 1)
            if response == None:
                chain[nums[i]] = -1
            
            if prev != None:
                chain[nums[i] - 1] = nums[i]

        
        return chain
    

class Solution:
    def longestConsecutive(self, nums):
        chain = set(nums)
        ans = 0

        for x in nums:
            if (x - 1) not in chain:
                y = x + 1
                while y in chain:
                    y += 1
                ans = max(ans, y - x)
            
        return ans
            



sol = Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))
print(set(nums))
        
        