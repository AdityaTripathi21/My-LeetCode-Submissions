"""Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.

brute force approach -> start from every square, consider all square sizes (1x1, 2x2, 3x3, and so on)
do this from every cell, that's m*n cells, and you can potentally explore the entire grid, so that's potentially m*n from every cell, so that's O(m*n)^2. This is a lot of repeated work because you check squares repeatedly which you already checked

instead of repeatedly checking the same square, we can store it using a cache -> top down memoization
let dp(r, c) = side length of largest square of 1s starting from the cell matrix[r][c]
 
for each cell, you need to know the answer to 3 other cells, the one to the right, the one down, and the right diagonal

so dp(r, c) = 1 + min(dp(r, c + 1), dp(r + 1, c), dp(r+1, c + 1))

base case -> out of bounds or matrix[r][c] == 0, if so, return 0

keep track of largest dp as you go, and in the end, square it and return"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:    # type: ignore
        rows = len(matrix)
        cols = len(matrix[0])
        cache = {}

        res = 0

        def dfs(r, c):
            if r == rows or c == cols:
                return 0

            if (r, c) in cache:
                return cache[(r,c)]

            if matrix[r][c] == "0":
                cache[(r, c)] = 0
                return 0
            
            right = dfs(r, c + 1)
            bottom = dfs(r + 1, c)
            diagonal = dfs(r + 1, c + 1)

            cache[(r, c)] = 1 + min(right, bottom, diagonal)

            return cache[(r, c)]

        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))

        return res * res