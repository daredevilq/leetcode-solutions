class Solution:
    def maxArea(self, height) -> int:
        start = 0
        end = len(height) - 1

        most_water = 0

        while start != end:
            width = end - start


            curr_height = min(height[start], height[end])
            most_water = max(most_water, curr_height*width)

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return most_water
    

height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(height))