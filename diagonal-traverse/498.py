from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        res = []
        going_up = True # track direction

        cur_row, cur_col = 0, 0

        while len(res) != rows * cols:
            if going_up:
                while cur_row >= 0 and cur_col < cols: 
                    res.append(mat[cur_row][cur_col])

                    cur_row -= 1
                    cur_col += 1
                
                if cur_col == cols: # col and row both out of bounds
                    cur_row += 2
                    cur_col -= 1
                else:               # row out of bounds
                    cur_row += 1
                
                going_up = False    # switch direction
            
            else:
                while cur_row < rows and cur_col >= 0:
                    res.append(mat[cur_row][cur_col])

                    cur_row += 1
                    cur_col -= 1
                
                if cur_row == rows:
                    cur_col += 2
                    cur_row -= 1
                else:
                    cur_col += 1
                
                going_up = True
            
        return res