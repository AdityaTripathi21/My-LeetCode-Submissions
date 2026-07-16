from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)    # dp[i] represents length of longest subsequence including that index

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)   # keep the best result, don't want it to get overwritten
        return max(dp)

    
                    
