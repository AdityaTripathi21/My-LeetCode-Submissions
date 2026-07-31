"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

1 <= nums.length <= 10^5 -> small
nums[i] is either 0 or 1

ex: nums = [0, 1, 0]
output = 2 because [0,1] or [1,0]

ex: nums = [0,1,1,1,1,1,0,0,0]
output = 6 because [1,1,1,0,0,0] (3 1s and 3 0s)

how to count subarray? prefix sums? no sum involved
need to keep track of 1s and 0s
actually wait, for len 2, sum has to be 1
res will only ever be even because we need equal number of 0s and 1s
so for len 6, sum has to be 3, for len 10, sum has to be 5, etc.

from this point onwards, needed a lil help
apparently convert 0 into -1
so all subarrays with equal frequency of 0s and 1s must sum to 0
=> subarray sum equals 0
still, how to keep track of longest subarray?

another hint: if two prefix sums at different positions have the same sum
the subarray between them must be 0, and so we need to find the longest one

my ramble:
so basically once you compute the prefix sum for a position, you have a hashmap that would check if it's been seen, and if it is, that value would be the index, so then you would calculate the different between the indices to get the length. However, if you have 3 prefix sums with the same value, how would you update the hashmap? like if I had sum of 1 at index 2 and then sum of 1 at index 7, and then I had a sum of 1 again at index 10, would I always just store the first value in the hashmap? I would right, I would never store the 7 as a key, only the 2

also you don't need a prefix array, I just do it just cuz, you can keep track of running sum with O(1) space
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        seen = {0: -1}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i - 1]
        
        for r in range(len(nums)):
            curr_sum = prefix[r]

            if curr_sum in seen:
                if r - seen[curr_sum] > res:
                    res = r - seen[curr_sum]
            else:
                seen[curr_sum] = r
        
        return res
        


        