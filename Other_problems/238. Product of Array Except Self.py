class Solution:
    def productExceptSelf(self, nums):
        leng = len(nums)

        left = [0] * leng
        right = [0] * leng
        result = []


        left[0] = nums[0]
        right[-1] = nums[-1]


        for i in range(1, leng):
            left[i] = left[i - 1] * nums[i]
            right[leng - i - 1] = right[leng - i] * nums[leng - i - 1]
        
        for i in range(leng):
            product = 1

            if i - 1 >= 0:
                product*= left[i - 1]
            if i + 1 < leng:
                product *= right[i + 1]
            
            result.append(product)

        return result


sol = Solution()
nums = [-1,1,0,-3,3]

print(sol.productExceptSelf(nums))