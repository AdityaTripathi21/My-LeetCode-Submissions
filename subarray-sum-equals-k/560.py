"""Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


1 <= nums.length <= 2 * 10^4 -> medium

-1000 <= nums[i] <= 1000 -> small

-10^7 <= k <= 10^7 -> large

[1, 1, 1], k = 2,
res = 2, [1, 1] and [1, 1]

obviously need to keep track of pointers so maybe sliding window? 

res: int to keep track of subarray count
probably only need to count subarrays and not keep track of the actual subarray

no sorting because we need to maintain the order

subarrays can range from 1 to len(nums) in size

l and r pointers start out at the same index 0

coming back to this problem after doing 303, we need prefix sums

so if we know that prefix[r] - prefix[l - 1] = k, we have a valid subarray [l, r] and can add that to res
however, iterating through every l and r value is still O(n^2), so we need to avoid the extra work
for every r, you check every l before r and check whether the prefix is valid, so for every r, it searches every previous position

to get rid of the nested loop, we fix r, so there's a loop for only r and not l
and so for every r, calculate the prefix sum, calculate the needed sum from prefix[r] - target = needed
check how many times needed appears in the hashmap, add that to res

for the hashmap, it's initialized with {0: 1} which represents the empty prefix when you start
for example, when you calculate needed and it's 0, it needs to already appear in the hashmap to count a valid sum
ex: [1,1], k = 2, if r = 1, we know that prefix[r] = 2, and needed = 2 - 2 = 0, so we need to keep 0 in the map,
otherwise [1,1] is missed"""



from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        seen = {0: 1}
        res = 0

        prefix[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i - 1]

        for r in range(len(nums)):
            curr_sum = prefix[r]

            needed = curr_sum - k

            if needed in seen:
                res += seen[needed]
            
            seen[curr_sum] = seen.get(curr_sum, 0) + 1
        
        return res

        
        