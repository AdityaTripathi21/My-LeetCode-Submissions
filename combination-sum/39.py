from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return 

            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, remaining - candidates[i])
                path.pop()
            
        dfs(0, [], target)
        return result