"""Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Brute force: Count every single subarray, there's n^2 subarrays. Not efficient
Repeated work in subarrays, so use prefix sums to make that more efficient

If a sum is divisible by k, that means subArray % k == 0. 
keep track of prefix sums, [0, 4, 9, 9, 7, 4, 5], the currPrefix - prevPrefix gives you the subarray sum from the element after prevPrefix to currPrefix, check if (currPrefix - prevPrefix) % k = 0, currPrefix % k = prevPrefix % k

We're looking for if we've already seen currPrefix % k in our map, and if we have, then we increment our count by how many times we've seen it, otherwise, we just add it to the map. Also, initialize the map with {0: 1}"""



class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix = {0: 1}
        curr_sum = 0
        count = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum % k in prefix:
                count += prefix[curr_sum % k]
                prefix[curr_sum % k] += 1
            else:
                prefix[curr_sum % k] = 1
        
        return count