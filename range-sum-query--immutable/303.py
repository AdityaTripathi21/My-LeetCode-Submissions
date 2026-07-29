"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.


Implement the NumArray class:

NumArray(int[] nums) 
Initializes the object with the integer array nums.

int sumRange(int left, int right) 
Returns the sum of the elements of nums between indices left and right inclusive 
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).


the naive approach: 
res = 0
        for i in range(left, right + 1):
            res += self.nums[i]
        return res

this is O(n) per query, if we have many queries, we may perform the same subarray sum many times
we can optimize queries to O(1) with prefix sums with O(n) space complexity through an array

fundamentally the concept of prefix sums is that you spend O(n) time complexity 
for O(1) space complexity for range queries. 

so you maintain a running total where prefix[i] = sum of all elements from the start plus nums[i]
so to answer range queries like nums[5] - nums[2], we can simply do prefix[5] - prefix[1] 
edge case: if left = 0, that means we can't do prefix[left - 1], so we just return prefix[right]
"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)
        self.prefix[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefix[i] = nums[i] + self.prefix[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)