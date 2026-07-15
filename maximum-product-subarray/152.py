from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 1,1

        for n in nums:
            tmp = cur_max * n
            cur_max = max(n, tmp, cur_min * n)  # use n for the 0 case
            cur_min = min(n, tmp, cur_min * n)
            res = max(res, cur_max)
        return res
