from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        def is_valid(r, c):
            if r - 1 >= 0 and c - 1 >= 0:
                return True
            else:
                return False

        for r in range(rows):
            for c in range(cols):
                if is_valid(r, c):
                    if matrix[r][c] == matrix[r-1][c-1]:
                        continue
                    else:
                        return False
        return True