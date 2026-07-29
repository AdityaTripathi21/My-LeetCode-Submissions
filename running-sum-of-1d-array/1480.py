"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

res is a list of the same size as nums that stores running totals for each position

res[i] = nums[i] + res[i - 1]

bruh 
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = nums[0]

        for i in range(1, len(nums)):
            res[i] = nums[i] + res[i - 1]

        return res
