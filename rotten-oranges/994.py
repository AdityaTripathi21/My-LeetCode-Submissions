from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        count = 0
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        def is_valid(r, c):
            return (0 <= r < len(grid) 
                and 0 <= c < len(grid[0]) 
                and grid[r][c] == 1)

        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                if is_valid(x - 1, y):
                    grid[x - 1][y] = 2
                    fresh -= 1
                    q.append((x - 1, y))

                if is_valid(x + 1, y):
                    grid[x + 1][y] = 2
                    fresh -= 1
                    q.append((x + 1, y))

                if is_valid(x, y + 1):
                    grid[x][y + 1] = 2
                    fresh -= 1
                    q.append((x, y + 1))

                if is_valid(x, y - 1):
                    grid[x][y - 1] = 2
                    fresh -= 1
                    q.append((x, y - 1))
            count += 1
        

        return count if fresh == 0 else -1