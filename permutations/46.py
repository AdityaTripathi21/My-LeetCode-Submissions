from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num in path:
                    continue
                
                path.append(num)
                dfs(path)
                path.pop()
        
        dfs([])
        return res