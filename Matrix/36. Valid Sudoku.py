class Solution:
    def isValidSudoku(self, board) -> bool:
        helper_array = [False] * 10
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    num = int(board[i][j]) 
                    if num > 9 or num < 1 or helper_array[num] == True:
                        return False
                    helper_array[num] = True

            helper_array = [False] * 10

        helper_array = [False] * 10

        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i] != ".":
                    num = int(board[j][i])
                    if num > 9 or num < 1 or helper_array[num] == True:
                        return False
                    helper_array[num] = True
            helper_array = [False] * 10

        helper_array = [False] * 10

        i = 0
        j = 0

        while i < len(board):
            while j < len(board[0]):
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] != ".":
                            num = int(board[i + k][j + l])
                            if num > 9 or num < 1 or helper_array[num] == True:
                                return False
                            helper_array[num] = True
                helper_array = [False] * 10
                j +=3
            i +=3

        return True
class Solution:
    def isValidSudoku(self, board) -> bool:
        # Initialize data structures to track seen digits
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    
                    # Check row
                    if num in rows[i]:
                        return False
                    rows[i].add(num)
                    
                    # Check column
                    if num in cols[j]:
                        return False
                    cols[j].add(num)
                    
                    # Check 3x3 box
                    box_index = (i // 3) * 3 + (j // 3)
                    if num in boxes[box_index]:
                        return False
                    boxes[box_index].add(num)
        
        return True

board = [[".",".",".",".",".",".","5",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         ["9","3",".",".","2",".","4",".","."],
         [".",".","7",".",".",".","3",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".","3","4",".",".",".","."],
         [".",".",".",".",".","3",".",".","."],
         [".",".",".",".",".","5","2",".","."]]



sol = Solution()
print(sol.isValidSudoku(board))