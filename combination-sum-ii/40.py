from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()


        def dfs(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return 

            if remaining < 0 or start == len(candidates):
                return
            
            path.append(candidates[start])
            dfs(start + 1, path, remaining - candidates[start])
            path.pop()

            while start + 1 < len(candidates) and candidates[start] == candidates[start + 1]:
                start += 1
            dfs(start + 1, path, remaining)
            
        dfs(0, [], target)
        return result