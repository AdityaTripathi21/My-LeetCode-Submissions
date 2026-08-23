"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

1 <= nums.length <= 100
0 <= nums[i] <= 400

small input -> large TC

at every index, we have 2 choies -> 
take that house and go to the i + 2 house
skip that house and go to i + 1 house

recurrence relation -> F(i) = max(F(i - 1), nums[i] + F(i - 2))
base case -> F(-1) = 0, F(-2) = 0
ex: [1, 2, 3, 1], F(0) = max(F(-1), 1 + F(-2)) = max(0, 1 + 0) = 1
F(1) = max(F(0), 2 + F(-1)) = max(1, 2 + 0) = 2
F(2) = max(F(1), 3 + max(0)) = max(2, 3 + 1) = 4
by the end, F(len(nums) - 1) will store the max money you can rob
define array of size len(nums) 
at the end, return dp[len(nums) - 1] or just dp[-1]

in the code, you can handle base cases differently by starting loop from index 2"""

class Solution:
    def rob(self, nums: List[int]) -> int:  # type: ignore
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]
