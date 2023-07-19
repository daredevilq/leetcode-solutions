class Solution:
    def trap(self, height):

        leftmax = [0] * len(height)
        rightmax = [0] * len(height)

        leftmax[0] = height[0]
        rightmax[len(height) - 1] = height[len(height) - 1]

        j = len(height) - 2
        for i in range(1,len(height)):
            leftmax[i] = max(leftmax[i - 1], height[i])
            rightmax[j] = max(rightmax[j + 1], height[j])
            j-=1

        water = 0
        for i in range(len(height)):
            water += min(leftmax[i],rightmax[i]) - height[i]

        return water




height = [0,1,0,2,1,0,1,3,2,1,2,1]

sol = Solution()
print(sol.trap(height))