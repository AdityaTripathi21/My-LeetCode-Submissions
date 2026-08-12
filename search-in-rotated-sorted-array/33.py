"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

array is initially sorted -> then left rotated

since we must write algo in O(lg n), need to use binary search (also searching in a sorted array)

since the full array is left sorted, it's not going to be in ascending order

nums = [4,5,6,7,0,1,2], target = 0
res = 4, 0 is at index 4

l = 0, r = len(nums) - 1 = 6
mid = (l + r) // 2 -> 3
so we check nums[3] - > 7
tells us nothing really because the array isn't sorted

ramble:
nums  = [6, 7, 0, 1, 2, 4, 5]
index =  0  1  2  3  4  5  6
let's say the target is 7, we know nums[mid] is 1, and then we check the right side, since nums[r] is greater than nums mid, we know that this side is sorted and the left side isn't (can you expand on why if one side is sorted, the other side is guaranteed to be not sorted). We check if target is within the range, and since it's not, we can drop this side of the array and go from l to mid - 1. And in that case the next mid will be 7, which is the target we're looking for. However let's say the target is 0. The array is currently [6,7,0] with l = 0, mid = 1, and r = 2. The left side is sorted and the target isn't in it, so we drop that side and check the right side

not fully accurate tho, because at least one side of the array is guaranteed to be sorted, 
however both could be sorted if you have an unrotated array or they're sorted like the first example

once you find the midpoint, use that to discern what side is sorted.
if the midpoint is less than the right, that side is sorted, check if target is between midpoint and r
    if not, set r = m - 1
if the midpoint is greater than the left, that side is sorted, check if target is between l and midpoint
    if not, set l = m + 1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[r]:  # right interval is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1

                else:
                    r = mid - 1

            else:                       # left interval is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1

                else:
                    l = mid + 1
            
        return -1
            


        