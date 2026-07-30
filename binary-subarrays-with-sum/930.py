"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

1 <= nums.length <= 3 * 10^4 - small
nums[i] is either 0 or 1.
0 <= goal <= nums.length

count the number of subarrays that sum up to goal
need prefix sums
the brute force approach is O(n^2) which checks every single subarray
we repeat a lot of sums, to optimize this, we can store those sums and get O(n) TC with O(n) SC
so we have a prefix array where prefix[i] stores the sum from the 0th to the ith element inclusive
for every single number, we can check all the numbers before using a hashmap
so we calculate the prefix sum for that number, check what we need with sum - goal
check if that's in the map, if it is, append it to the res, and then also add the current sum to the hashmap
the map must also contain {0: 1} because it helps with counting sums starting from the start

after solving, i realized you can use sliding window with o(1) time which is way more efficient,
will solve this agains someday
"""

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        seen = {0: 1}
        res = 0

        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i - 1]

        for r in range(len(nums)):
            curr_sum = prefix[r]
            
            needed = curr_sum - goal

            if needed in seen:
                res += seen[needed]
            
            seen[curr_sum] = seen.get(curr_sum, 0) + 1
        
        return res
        
        
        