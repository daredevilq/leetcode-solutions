class Solution:
    def setZeroes(self, matrix) -> None:
        rows = {}
        cols = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                set_zero_row = rows.get(i)
                set_zero_col = cols.get(j)
                
                if set_zero_col != None or set_zero_row != None:
                    matrix[i][j] = 0
        
        