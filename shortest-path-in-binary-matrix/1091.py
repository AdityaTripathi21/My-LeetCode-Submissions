from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
            return -1

        def is_valid(r, c):
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]):
                return False
            if grid[r][c] == 1:
                return False
            return True

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1), (1, -1),  
            (1, 0),  (1, 1)
        ]

        q = deque([(0, 0, 1)])

        while q:
            r, c, distance = q.popleft()

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return distance

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if is_valid(nr, nc):
                    grid[nr][nc] = 1
                    q.append((nr, nc, distance + 1))
        return -1
