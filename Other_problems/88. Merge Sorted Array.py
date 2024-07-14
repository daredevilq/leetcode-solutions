class Solution:
    def merge(self, nums, m, nums2, n):
        if n == 0:
            print(nums)
            return
        
        if m == 0:
            for i in range(n):
                nums[i] = nums2[i]
            print(nums)
            return
        
        i = 0
        j = 0
        k = 0

        arr = []
        while k < n + m:
            if i < m and j < n:
                if nums[i] < nums2[j]:
                    arr.append(nums[i])
                    i+=1
                else:
                    arr.append(nums2[j])
                    j+=1
            elif i < m:
                arr.append(nums[i])
                i+=1
            elif j < n:
                arr.append(nums2[j])
                j+=1
            k+=1
    

        for i in range(len(arr)):
            nums[i] = arr[i]


     
    


sol = Solution()


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sol.merge(nums1, m, nums2, n)





