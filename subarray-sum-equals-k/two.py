""" Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [1,2,3], k = 3
Output: 2 -> [1, 2], [3]

1 <= nums.length <= 2 * 10^4 -> small-ish
-1000 <= nums[i] <= 1000    -> small
-10^7 <= k <= 10^7  -> large

elements must be consecutive

brute force -> check all subarrays, so for [1,2,3], I would start from [1], then [1,2], then [1,2,3],
then I would move to [2], then [2,3], and then [3], this is O(n^2) TC, because you check n + n - 1 + n - 2 + ... 1

how to optimize this? Clearly there is repeated work, for example, I already have computed [1,2] and then I recompute it again for [1,2,3], so maybe I can find a way to save that computation and get rid of unecessary work

how tho?

prefix sums -> ex: [1,2,3] - > [0, 1, 3, 6], subarraySum = currPrefix - prevPrefix, we want subarraySum = k,
so k = currPrefix - prevPrefix, => prevPrefix = currPrefix - k, so as we go through the array, check if we've seen a previous sum that is equal to the current sum - k, we need quick lookups for this, so use a map, and we can calculate all of this in one pass, so TC is O(n), and SC is O(n) for the map. Note: make sure to increment the count by how many times you've already seen the previous and not by 1.
"""



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:  # type: ignore
        prefix = {0:1}
        count = 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            needed = curr_sum - k
            if needed in prefix:
                count += prefix[needed]
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
        return count