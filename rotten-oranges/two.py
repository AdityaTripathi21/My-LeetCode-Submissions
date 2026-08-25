"""You are given an m x n grid where each cell can have one of three values:


0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

m == grid.length
n == grid[i].length
1 <= m, n <= 10 -> no need to account for empty grid
grid[i][j] is 0, 1, or 2.

grid can have multiple rotten oranges to start
how can we check we rot every fresh orange? 
traverse through the loop once, count every rotten orange and count every fresh orange
at the very end of our algorithm, assuming it's successful, if there's still fresh oranges, then return -1
for every rotten orange we find initially, we need to use a queue and enqueue it, and then we can run multi source bfs
need variable for time as well"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int: # type: ignore
        fresh = 0
        time = 0
        q = deque() # type: ignore

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:   # rotten
                    q.append((i, j))

                if grid[i][j] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            level = len(q)

            for i in range(level):
                r, c = q.popleft()

                for dr, dc in directions:
                    x, y = r + dr, c + dc
                    if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                        if grid[x][y] == 1:
                            fresh -= 1
                            grid[x][y] = 2
                            q.append((x,y))
            
            time += 1
        
        if fresh:
            return -1
        return time
                
                    
            
