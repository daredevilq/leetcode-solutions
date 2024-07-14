import bisect


def recursive_binary_sort(T, l, r, x):
    if r >=l:
        mid = (l + r)//2
    
        if T[mid] == x:
            return mid
        elif T[mid] < x:
            return recursive_binary_sort(T, mid + 1, r, x)
        elif T[mid] > x:
            return recursive_binary_sort(T, l, mid - 1, x)
    else:
        return -1
    


def iterative_binary_sort(T, l, r, x):
    while r>=l:
        mid = (r + l)//2

        if T[mid] == x:
            return mid
        elif T[mid] > x:
            r = mid - 1
        elif T[mid] < x:
            l = mid + 1
    return -1


class Solution:

    def iterative_binary_sort(self, T, l, r, x):
        while r>=l:
            mid = (r + l)//2

            if T[mid] == x:
                return mid
            elif T[mid] > x:
                r = mid - 1
            elif T[mid] < x:
                l = mid + 1
        return -1


    def countSmaller(self, nums):
        result = [0] * len(nums)
        map = {}

        copy_nums = nums.copy()
        copy_nums.sort()
        
        print(copy_nums)
        print(nums)

        for i in range(len(nums)):
            map[nums[i]] = i

        print(map)

        for i in range(len(nums)):
            searching_num = nums[i]

            smaller_numbers_no = self.iterative_binary_sort(copy_nums, 0, len(copy_nums) - 1, searching_num)

            result[map.get(searching_num)] = smaller_numbers_no 

        return result



class Solution:
    def countSmaller(self, nums):
        
        result = [0]*len(nums)
        sorted_arr = []
        for i in range(len(nums) - 1, -1, -1):
            index = bisect.bisect_left(sorted_arr, nums[i])
            bisect.insort_left(sorted_arr, nums[i])
            result[i] = index

        return result

sol = Solution()

nums = [5,2,6,1]



print(sol.countSmaller(nums))