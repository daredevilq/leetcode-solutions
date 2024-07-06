class Solution:
    def threeSum(self, nums):
        dict = {}
        helper_dict = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                index = nums[i] + nums[j]
                if nums[i] < nums[j]:
                    left = nums[i]
                    left_index = i
                    
                    right = nums[j]
                    right_index = j
                else:
                    left = nums[j]
                    left_index = j

                    right = nums[i]
                    right_index = i
                if dict.get(index) == None:
                    dict[index] = [(left, right, left_index, right_index)]
                else:
                    dict[index].append((left, right, left_index, right_index))

        pre_result = []
        for k in range(len(nums)):
            twos = dict.get(-nums[k])

            if twos != None:
                for (num_i, num_j, i, j) in twos:
                    if i != j and i != k and j != k:
                        if nums[k] < num_i and helper_dict.get((nums[k],num_i,num_j)) == None:
                            pre_result.append([nums[k],num_i,num_j])
                            helper_dict[(nums[k],num_i,num_j)] = True
                        elif num_i < nums[k] and nums[k] < num_j and helper_dict.get((num_i,nums[k],num_j)) == None:
                            pre_result.append([num_i,nums[k],num_j])
                            helper_dict[(num_i,nums[k],num_j)] = True
                        elif helper_dict.get((num_i,num_j,nums[k])) == None:
                            pre_result.append([num_i,num_j,nums[k]])
                            helper_dict[(num_i,num_j,nums[k])] = True
                        
        return pre_result



class Solution:
    def threeSum(self, nums):
        # First, sort the array
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))



