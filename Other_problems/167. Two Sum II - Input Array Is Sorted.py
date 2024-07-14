class Solution:
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers) - 1

        while True:
            if numbers[start] + numbers[end] == target:
                break
            elif numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1

        return [start + 1, end + 1]
    






numbers = [-1,0]
target = -1
sol = Solution()
print(sol.twoSum(numbers, target))