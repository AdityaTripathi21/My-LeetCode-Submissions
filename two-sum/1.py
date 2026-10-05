"""You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

brute force: consider all 2 elements, this is n^2 subarrays, so O(n^2)
to get rid of repeated work, we should remember what we have seen, so use maps

every single time we look at a element, we check what we need, so if I'm at 2, I need 9 - 2 = 7, check if 7 is in the map, it's not, so just add 2 to the map, and then when I go to 7, check what I need, 2, check if in map, see it is, get value of both and return"""



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:    # type: ignore
        answer_map = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in answer_map:
                return [i, answer_map[needed]]
            else:
                answer_map[nums[i]] = i