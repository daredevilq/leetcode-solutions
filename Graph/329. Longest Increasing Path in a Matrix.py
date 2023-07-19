class Solution:
    def longestIncreasingPath(self, matrix):
        memo = {}
        def recursion(y,x):
            if (y,x) in memo:
                return memo[(y,x)]
            
            res = 0
            
            if x + 1<len(matrix[0]) and matrix[y][x]<matrix[y][x+1]:
                res = max(res, recursion(y, x+1)) + 1

            if x - 1 >=0 and matrix[y][x]<matrix[y][x-1]:
                res = max(res, recursion(y, x-1) ) + 1

            if y + 1 < len(matrix) and matrix[y][x]<matrix[y+1][x]:
                res = max(res, recursion(y + 1, x) ) + 1 
            
            if y - 1 >= 0 and matrix[y][x]<matrix[y-1][x]:
                res = max(res, recursion(y - 1, x) ) + 1

            
            memo[(y,x)] = res
            return res
        

        answer = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                answer = max(answer, recursion(i,j))
        
        return answer + 1
    




matrix = [[3,4,5],[3,2,6],[2,2,1]]

sol = Solution()

print(sol.longestIncreasingPath(matrix))