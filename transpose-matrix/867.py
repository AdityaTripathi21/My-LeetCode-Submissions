from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        t = [[0 for _ in range(m)] for _ in range(n)]

        for r in range(m):
            for c in range(n):
                t[c][r] = matrix[r][c]
        
        return t