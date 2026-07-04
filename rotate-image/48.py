from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                top_left = matrix[top][l + i]
                
                top_right = matrix[top + i][r]

                bottom_right = matrix[bottom][r - i]

                bottom_left = matrix[bottom - i][l]
                
                matrix[top + i][r] = top_left

                matrix[bottom][r - i] = top_right

                matrix[bottom - i][l] = bottom_right

                matrix[top][l + i] = bottom_left
            l += 1
            r -= 1
