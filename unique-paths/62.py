"""There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

1 <= m, n <= 100

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

base case: either m = 1 or n = 1, then there's only 1 way
every single time you move down or right, you subtract from m or n by 1

Let's define recurrence as F(m,n) = number of paths through m * n grid
if you start from the top-left corner and move to the bottom-right, you can either choose to go down or right,
but you can't choose both at the same time, => F(m,n) = F(m - 1, n) + F(m, n - 1)
That is the recurrence relation, and you go till you hit the base case where m = 1 or n = 1, 
however, you will also end up calculating the same F(m,n) many times, so we can use memoization to save in TC"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def helper(m, n):
            if m == 1 or n == 1:
                return 1
            
            if (m, n) not in memo:
                memo[(m, n)] = helper(m - 1, n) + helper(m, n - 1)
            
            return memo[(m, n)]
        
        return helper(m, n)