"""Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

1 <= nums.length <= 10  -> small input arr -> big time complexity
-10 <= nums[i] <= 10
All the numbers of nums are unique. -> no need to check conditions

at every possible index, we have 2 choices, take or not take
build result with that

need array for the entire res, need array for each path as well

choices -> take element or skip
constraints -> none
base case -> reached end of list
backtrack -> remove element and explore other paths"""



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:  # type: ignore
        res = []
        path = []

        def helper(index, path):
            if index == len(nums):
                res.append(path[:]) # append copy because path is mutable
                return

            # no constraints

            # choice 1
            path.append(nums[index])
            helper(index + 1, path)

            # backtrack
            path.pop()

            # choice 2
            helper(index + 1, path)
        
        helper(0, path)
        return res
