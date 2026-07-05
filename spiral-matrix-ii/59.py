from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        counter = 1

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            # top row
            for i in range(left, right):
                matrix[top][i] = counter
                counter += 1
            
            top += 1

            # right col
            for i in range(top, bottom):
                matrix[i][right - 1] = counter
                counter += 1
            
            right -= 1
                        
            # bottom row
            for i in range(right - 1, left - 1, -1):
                matrix[bottom - 1][i] = counter
                counter += 1
            
            bottom -= 1

            # left col
            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = counter
                counter += 1
            
            left += 1

        return matrix