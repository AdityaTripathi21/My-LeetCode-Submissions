"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

m == grid.length
n == grid[i].length
1 <= m, n <= 300    -> no empty grid
grid[i][j] is '0' or '1'.

an island is any number of 1s surrounded by 0s on 4 sides

how to count islands?
need recursive dfs for this

maybe keep visited set? or just change 1s to 0s 
so every single time you see a 1, you increase the number of islands by 1
you recurse from that 1 to cover the entire island and mark it as visited

loop through every element

marking cells as visited by changing them to 0 is more space efficient than using a set
using recursion, the TC is still O(n*m), you have to visit every cell and then the 
DFS fully processes every land cell so worst case 
if every cell is land, the dfs still only does O(n*m) total work
the worst case SC is O(n*m) if the call stack for recursion grows very large due to every cell being land"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: # type: ignore 

        def helper(r, c):
            if r < 0 or r >= len(grid) or  c < 0 or c >= len(grid[0]):
                return 
            if grid[r][c] == "0":
                return 
            if grid[r][c] == "1":
                grid[r][c] = "0"  # mark as visited

            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c - 1)
            helper(r, c + 1)
        
        num_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_of_islands += 1
                    helper(i, j)
        
        return num_of_islands
        
