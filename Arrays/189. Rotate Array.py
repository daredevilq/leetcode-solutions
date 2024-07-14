


class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy_arr = nums.copy()

        n = len(nums)
        for i in range(len(nums)):
            nums[(i+k)% n] = copy_arr[i]


        return nums
    


sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(sol.rotate(nums, k))
