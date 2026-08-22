"""Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

1 <= nums.length <= 6 -> small input size -> large TC
-10 <= nums[i] <= 10   
All the integers of nums are unique. -> can't repeat elements

choices -> choose any element as long as it's not already used
constraints -> if already in current path, skip
base case -> pos == len(nums)
backtrack -> can't go by index from start to finish, you can go by index, but if you start from index 1, you can go back to index 0, so if you start from a non zero index, you should reset from 0 and just skip over elements already in list. Instead of going by index, go by pos that needs to be filled


"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:  # type: ignore
        res = []
        path = []
        used = set()

        def helper(pos):
            if pos == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                
                path.append(nums[i])
                used.add(i)
                helper(pos + 1)
                used.remove(i)
                path.pop()

        helper(0)
        return res

            
        