"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

1 <= n <= 200 - each array is small

-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28 - elements are large

O(n^4) trivial solution -> how to optimize??
would sorting help? -> don't think so

res: int -> count

regular 4sum is one entire array and you fix indices and then use 2 pointers
4sum II is about multiple arrays of the same length, so idt you can use 2 pointers
maybe hashmap, but how?? 

nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0
so, nums1[i] + nums2[j] = -(nums3[k] + nums4[l])
so if we hash i and j pairs, that's only n^2 pairs, and n <= 200, so it's manageable
hashmap: pair_sum -> number of (i,j) pairs because we care about the number of tuples
so now we only have to loop through nums3 and nums4 which is O(n^2) so we look for the negative of their sum
"""

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        pair_sum = {}
        res = 0
        
        for a in nums1:
            for b in nums2:
                pair = a + b
                pair_sum[pair] = pair_sum.get(pair, 0) + 1

        for c in nums3:
            for d in nums4:
                pair = c + d
                if -pair in pair_sum:
                    res += pair_sum[-pair]
        
        return res