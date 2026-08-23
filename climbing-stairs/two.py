"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

1 <= n <= 45 -> small -> large TC

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


for n = 1, there's only one way, for n = 2, there's 2 ways (1 step 1 step, 2 step), for n = 3, there's 3 ways
(1 + 1 + 1), (1 + 2), (2 + 1)

the base cases are clearly n = 1, and n = 2, there's 1 and 2 ways respectively. Every other n, there's a subproblem

num of ways(n) = num of ways(n - 1) + num of ways(n - 2)
this is the recurrence relation

also need to optimize since TLE, we can store already known calls with a map
"""

class Solution:
    def climbStairs(self, n: int) -> int:   
        memo = {1: 1, 2: 2}

        def num_of_ways(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = num_of_ways(n - 1) + num_of_ways(n - 2)
            
            return memo[n]

        return num_of_ways(n)