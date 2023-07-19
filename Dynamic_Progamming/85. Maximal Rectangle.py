class Solution:
    def maximalRectangle(self, matrix):
        def max_histogram(lvl, matrix):
            height = [0] * len(matrix[0])

            for i in range(len(matrix[0])):
                for j in range(lvl, len(matrix)):
                    if matrix[j][i] == "0":
                        break
                    height[i] += 1
            
            
            left = [0] * len(matrix[0])
            right = [len(matrix[0])-1] * len(matrix[0])
            left[0] = 0
             
            for i in range(len(matrix[0])):
                for j in range(i ,-1,-1):
                    if height[j]<height[i]:
                        left[i] = j + 1
                        break
            
            for i in range(len(matrix[0])):
                for j in range(i ,len(matrix[0])):
                    if height[j] < height[i]:
                        right[i] = j -1 
                        break

            area = -1
            for i in range(len(height)):
                area = max(area, (abs(right[i] - left[i]) + 1) * height[i] )
            return area
        
        best = -1
        for i in range(len(matrix)):
            best = max(best, max_histogram(i,matrix))
        
        return best
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]


sol = Solution()
print(sol.maximalRectangle(matrix))


