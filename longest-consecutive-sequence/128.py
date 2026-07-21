from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0

        num_set = set()

        for n in nums:
            num_set.add(n)
        
        curr = 0
        best = 0

        for n in num_set:
            if n - 1 not in num_set:
                i = 1
                curr = 1
                while n + i in num_set:
                    curr += 1
                    i += 1
                if curr > best:
                    best = curr
        
        
        return best
        

                
        