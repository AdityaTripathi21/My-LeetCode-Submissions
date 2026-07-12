from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:  # edge case where there's only 1 house
            return nums[0]
        
        def rob(nums):
            prev_1 = 0   # first house
            prev_2 = 0   # second house

            for money in nums:
                curr = max(prev_2, prev_1 + money)
                prev_1 = prev_2
                prev_2 = curr
            
            return prev_2
        
        return max(rob(nums[:len(nums) - 1]), rob(nums[1:]))
