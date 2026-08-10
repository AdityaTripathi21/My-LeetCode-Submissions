"""Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

1 <= nums.length <= 10^5 -> small/medium-ish
nums[i] is either 0 or 1.
0 <= k <= nums.length


nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
       [1,1,1,0,0,1,1,1,1,1,1], res = 6
    
variable sized window (obviously)
trace -> 1, 1, 1, 0, 0
already seen 2 zeroes, so k = 0, subtract k every single time you see 0
see next 0, k already 0, so I need to move window (aka left pointer until k is 1)

keep track of best window

man
either the number is 0 or 1
if it's 0, check if we can flip or if we can't
if we can flip, just take 1 off k
if we can't flip, then while the left pointer isn't 0, increment it
it will land on the first 0 in the window, increment it again to move past it
notice: didn't update k at all, because the window is already full and was overloaded before
now k is still 0, but the window is valid

"""


from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0

        best = 0
        cur = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                if k > 0:
                    k -= 1
                else:
                    while nums[l] != 0:
                        l += 1
                    
                    l += 1
            
            cur = r - l + 1
            best = max(best, cur)
        
        return best
            
            

        
        