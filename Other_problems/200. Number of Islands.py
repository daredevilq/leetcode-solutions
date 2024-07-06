class Solution:
    def numIslands(self, grid) -> int:
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    up_y = i - 1
                    up_x = j
                    left_x = j - 1
                    left_y = i

                    up_flag = False
                    left_flag = False

                    if (up_y < 0 or up_x < 0):
                        up_flag = True
                    else:
                        if(grid[up_y][up_x] == "0"):
                            up_flag = True

                    if (left_x < 0 or left_y < 0):
                        left_flag = True
                    else:
                        if (grid[left_y][left_x] == "0"):
                            left_flag = True

                    if left_flag and up_flag:
                        islands+=1                        

        return islands



class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Right, Left, Down, Up
        islands = 0
        
        def dfs(x, y):
            grid[y][x] = "0"  # Mark the cell as visited
            for (dx, dy) in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == "1":
                    dfs(nx, ny)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(j, i)

        return islands

# Example usage:
sol = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(sol.numIslands(grid))  # Output: 1



