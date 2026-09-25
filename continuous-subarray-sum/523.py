"""Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

1 <= nums.length <= 10^5 -> medium
0 <= nums[i] <= 10^9    -> big
0 <= sum(nums[i]) <= 2^31 - 1   -> big
1 <= k <= 2^31 - 1  -> big

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Need prefix sums obviously, pretty similiar to 560 in that regard.
Only subarray of at least length 2 must be considered, and also subarray sums % k == 0. 0 counts as a mutliple
Use a map for prefix lookups, so subArrSum = currPrefix - prevPrefix, => prevPrefix = currPrefix - subArrSum.
In this case, we want the sum to be a multiple of k, so we can just use k for subArrSum, because subtracting k will give you another multiple of k if prevPrefix is valid. So we are looking for prevPrefix = currPrefix - k, and prevPrefix must at least have length 2 as well. Length 2 is the biggest challenge in this problem. 

Walk through arr: 0, 23, 23 - 6 = 17, 17 not divisible by k = 6, so move on, store 23 as prefix sum, 23 + 2 = 25, 25 - 6 = 19, 19 not divisible by k, store 25 as prefix sum, 25 + 4 = 29, 29 - 6 = 23, 23 not divisible by 6, move on, wait this is completely wrong. I shouldn't check if 23 is divsible by 6, just check if it's already been seen.

to figure out if a subarray is valid, you can still do currPrefix - prevPrefix, but you should check if that is a multiple of k. So in this case, the currPrefix is 29 after 4, and then the prevPrefix is 23 after 23, their difference is 29 - 23 = 6, which is a multiple of k. 

Needed help on this part, but (currPrefix - prevPrefix) mod k = 0. so currPrefix mod k = prevPrefix mod k, so in this case, 29 mod 6 = 23 mod 6 = 5. So the map should store where the earliest index of each remainder is. 

This is the same idea as LC 560, however when you do currPrefix - prevPrefix = k, you could potentially miss a lot of good subarrays because we also need multiples of k, so we need currPrefix - prevPrefix to be divisble by k, so (currPrefix - prevPrefix) mod k = 0. So this means we need currPrefix mod k = prevPrefix mod k, so we need to check for remainders and if we've seen them before, and so we design our map around that. We only store the earliest seen remainder if we've seen the same one multiple times, because we want the greatest distance between indices to maximize the chances of having a good subarray, and the map lets us access indices quickly. One small thing: we need to store the prefix before the array as {0: -1} in the map. """

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix = {0: -1}
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum % k in prefix:
                if i - prefix[curr_sum % k] >= 2:
                    return True
            else:
                prefix[curr_sum % k] = i
        
        return False

        