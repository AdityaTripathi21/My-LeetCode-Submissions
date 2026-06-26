from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean):
            ocean.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0 or nr == rows or
                    nc < 0 or nc == cols or
                    (nr, nc) in ocean or
                    heights[nr][nc] < heights[r][c] # since it's opposite, if the height is less, we ignore it
                ):
                    continue

                dfs(nr, nc, ocean)

        for c in range(cols):
            dfs(0, c, pacific)          # top row
            dfs(rows - 1, c, atlantic) # bottom row

        for r in range(rows):
            dfs(r, 0, pacific)         # left col
            dfs(r, cols - 1, atlantic) # right col

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
