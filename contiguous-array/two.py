""" Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 Observation: valid subarrays can only be even in length starting from 2, and then must sum up to len(subArray)/2,
 so for example, [0, 1] sums up to 1, [0, 1, 1, 0] sums up to 2

 Brute force, just consider every single even length subarray, so ex: [0,1,1,1,1,1,0,0,0], start from
 [0,1 ], [0, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 0], and then start from the first 1 and do the same thing. This is n^2 subarrays so O(n^2). Again, there is a lot of repeated work, so maybe we could use prefix sums, so if there is a sum of 1 with a length of 2, you know for sure that's valid, and if there is a sum of 2 with a length of 4, you know that's valid. So if subArraySum = currPrefix - prevPrefix, and we can use a map to store indices.

Need map to have indices

If there are an even number of 1s and 0s, if we treat 0s as 1s, the subarray sum should cancel out to 0.
We want the largest subarray in length.

 [0, 1, 1, 0, 1, 0]
    [-1, 1, 1, -1, 1, -1]
  [0, -1, 0, 1, 0, 1, 0]
  Every single time you encounter the same sum in the prefix array, that means that everything between those sums cancels out, which means there's an equal number of 1s and 0s. Since we also want to maximize the distance, when we store the indices in our map, we store the earliest seen index of that element. Checking the length of the subarry would then be just checking curr_index - prefix[prefix_sum]. prefix is a map that stores the earliest seen index of a prefix sum value. Prefix also needs to store {0: -1} to calculate subarrays starting from the beginning correctly. """

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:    # type: ignore
        prefix = {0: -1}
        curr_sum = 0
        best = 0

        for i in range(len(nums)):
            if nums[i] == 0:    # 0
                curr_sum -= 1
            else:               # 1
                curr_sum += 1

            if curr_sum in prefix:
                candidate = i - prefix[curr_sum]
                best = max(candidate, best)
            else:
                prefix[curr_sum] = i
                
        return best

