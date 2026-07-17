from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # diagonal starting on left edge
        for row in range(n):
            r = row
            c = 0
            diagonal = []

            while r < n and c < n:
                diagonal.append(grid[r][c])
                r += 1
                c += 1

            diagonal.sort(reverse=True)
            r = row
            c = 0
            i = 0

            while r < n and c < n:
                grid[r][c] = diagonal[i]
                i += 1
                r += 1
                c += 1
        
        # diagonal starting on top edge
        for col in range(1, n):
            c = col
            r = 0
            diagonal = []


            while r < n and c < n:
                diagonal.append(grid[r][c])
                r += 1
                c += 1

            diagonal.sort()
            c = col
            r = 0
            i = 0

            while r < n and c < n:
                grid[r][c] = diagonal[i]
                i += 1
                r += 1
                c += 1
    
        return grid