"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10^-5 will be accepted.

1 <= k <= n <= 10^5 -> n is small-ish, k can never be greater than n, so don't have to handle that

-10^4 <= nums[i] <= 10^4 -> elements are small-ish

maintain window of size k and just iterate through the whole array
so it'll be O(n) TC and O(1) SC

start with left pointer at 0, right pointer at k - 1, 
find the sum, and just divide by k, instead of recomputing the entire sum every time,
just subtract left and move the left pointer, and then add the next element to the right pointer and move the pointer
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        res = window_sum

        for r in range(k, len(nums)):
            window_sum += nums[r]
            window_sum -= nums[r - k]
            res = max(window_sum, res)
        
        return res / k
            