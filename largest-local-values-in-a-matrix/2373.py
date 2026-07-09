from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        max_local = [[0 for _ in range(n - 2)] for _ in range(n-2)] # max_local has dim (n-2, n-2)

        for r in range(n - 2):  # only go to n - 2 otherwise 3x3 filter is out of bounds
            for c in range(n-2):
                curr = 0
                for x in range(r, r + 3):   # consider the best values in a 3x3 grid
                    for y in range(c, c + 3):
                        curr = max(curr, grid[x][y])
                max_local[r][c] = curr
                        


        return max_local