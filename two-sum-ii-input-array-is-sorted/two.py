"""You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.

Find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2 as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Use 2 pointers since the array is sorted, start from l = 0, and then r = len(numbers) - 1
if l + r == target, return [l + 1, r + 1], elif l + r < target, l += 1, else, r -= 1
use while loop l < r, if condition flips so l > r, that means we have visited every element
O(n) time because we can potentially go through the entire array, o(1) space
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]: # type: ignore
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1