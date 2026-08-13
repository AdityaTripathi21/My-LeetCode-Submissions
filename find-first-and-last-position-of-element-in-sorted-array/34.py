"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

0 <= nums.length <= 10^5 -> small/medium-ish
-10^9 <= nums[i] <= 10^9 -> doesn't really matter

nums is a non-decreasing array. -> important

O(lg n) -> binary search

since the array is already sorted in non-decreasing order -> we can apply binary search

res = array of len 2, initialize with [-1, -1]

once we find target using binary search, we need to find the first and last occurence as well
we could use a while loop and use l and r pointers to go in both directions, but I feel like this is a naive approach

maybe we could run binary search again: ex [7, 8, 8, 8, 8, 8, 9]
let's say we land on the middle 8, then we need a way to run binary search again
run it on [7, 8, 8, 8] -> l to mid
run it on [8, 8, 8, 9] -> mid to r

[7, 8, 8, 8] -> mid = 1, so nums[1] -> 8
since this is the left hand side, we only want to run it again on the left and not the right

[7, 8] -> mid = 0, so nums[0] -> 7
mid isn't equal to target so the previous mid is the first

do the same thing on the right hand side


knew the approach but struggled with implementing it cleanly


"""



from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                res[0] = m
                r = m - 1

            
            elif nums[m] < target:
                l = m + 1
            
            else:
                r = m - 1
        

        l = 0
        r = len(nums) - 1


        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                res[1] = m
                l = m + 1
            
            elif nums[m] < target:
                l = m + 1
            
            else:
                r = m - 1
    
        return res
            
            