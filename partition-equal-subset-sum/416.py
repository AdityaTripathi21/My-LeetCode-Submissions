from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        half_sum = sum(nums) // 2  # both subsets must be equal to this

        achievable_sums = set() 
        achievable_sums.add(0)  # base - we skip all numbers

        for num in nums:
            next_sums = achievable_sums.copy()  # skip the number

            for current_sum in achievable_sums: # use the number
                new_sum = current_sum + num

                if new_sum == half_sum: # if we found a half_sum we know that the rest of the array must be valid
                    return True
                
                if new_sum < half_sum:
                    next_sums.add(new_sum)
            achievable_sums = next_sums

        return False