"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

1 <= nums.length <= 50000 -> small
1 <= nums[i] <= 10^5 -> small
1 <= k <= nums.length 


nums = [1,1,2,1,1], k = 3
res = 2
The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

ramble:
For LC 1248, you shouldn't sum anything up even though it's a prefix sum problem right? I'm trying to solve it by myself so don't give me the solution or any hints. I was thinking that you keep track of how many odd numbers you've seen up to a point instead of keeping track of the sum. So for ex: [1,1,2,1,1], k = 3. If we build the counter array, it would be [1, 2, 2, 3, 4], so we know that once we first hit 3, that counts, and then when we get to 4, we check what we need for k, so we need 4 - 3 = 1, and we check if 1 is in the hashmap, and it is, so we can include the one from the 2nd index onwards.

so basically instead of summing everything up, we keep track of how many odd numbers we've seen
also need a map for keeping track of the needed odd count where the value is the number of positions it occured

[1, 1, 2, 1, 1, 1]
[1, 2, 2, 3, 4, 5]

great example above

this example shows that how the map should be constructed
"""




from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        seen = {0: 1}
        
        odd = [0] * len(nums) 

        if nums[0] % 2 != 0:
            odd[0] = 1

        for i in range(1, len(nums)):
            if nums[i] % 2 != 0:
                odd[i] = odd[i - 1] + 1
            else:
                odd[i] = odd[i - 1]
        
        for r in range(len(nums)):
            odd_count = odd[r]
            needed = odd_count - k

            if needed in seen:
                res += seen[needed]
            
            seen[odd_count] = seen.get(odd_count, 0) + 1

        return res



        