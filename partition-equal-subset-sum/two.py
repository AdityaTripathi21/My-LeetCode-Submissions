"""Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

1 <= nums.length <= 200 -> small input -> large TC
1 <= nums[i] <= 100

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

both sides must sum to total / 2
so if the sum is ever odd, just return false immediately

instead of trying to find both sides that sum up to the total // 2
I only need to find a subset that sums up to half
because then the other half must be equal and I have partitioned the array successfully
don't actually need to find the partitions, just need to return true or false

the problem then becomes can I find a subset that sums up to total // 2?
What changes between each state as you move through the array?
The index and the sum
Instead of using index, we can use the first i numbers
So, F(i, s) answers whether I can make sum s using the first i numbers
the current index will be nums[i - 1], but that isn't important yet
F(i, s) returns bool (T/F), and to figure out F(i, s) you need to think about either skipping or taking that element
If you skip it -> You need to figure out if you can make s from the first i - 1 numbers, so F(i - 1, s)
if you take it -> You need to figure out if you can make s - nums[i - 1] from the first i - 1 numbers, 
so F(i - 1, s - nums[i - 1]), however this is only possible if s - nums[i - 1] >= 0
so then you can write the recurrence as F(i, s) = F(i - 1, s) OR F(i - 1, s - nums[i - 1])

base case -> F(i, 0) = True, you can always create a sum of 0 using any number of elements by skipping all of them
base case -> F(0, s) = False, you can't create any sum with 0 elements available, note: only true for s > 0

NOTE: i doesn't mean use all of the first i elements, it means use any subset

Therefore, the question is F(len(target), sum(nums) // 2)
also, use memo for caching (i, s) calls
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:    # type: ignore
        total = sum(nums)
        memo = {}

        if total % 2 != 0:
            return False
        

        def helper(i, s):
            if s == 0:
                return True
            
            if i == 0 and s:
                return False
            
            if (i, s) not in memo:
                if s - nums[i - 1] < 0: # you can only skip because the current number is too big
                    memo[(i, s)] = helper(i - 1, s)
                else:
                    memo[(i, s)] = helper(i - 1, s) or helper(i - 1, s - nums[i - 1])
            
            return memo[(i, s)]
        

        return helper(len(nums), total // 2)
        


        