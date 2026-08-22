"""Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

need res list and need cur path list
don't need additional argument for target because we can keep subtracting from target, so we need argument for remaining
so if target is ever equal to 0, that means we found a valid path, append it to res, and return

why is this backtracking? small input -> large complexity, we need to find combinations, need to keep trying diff combinations, and if we find dead ends, return back and undo the choice

since we can reuse candidates, we need to scan all of them every single time 
however, we need to avoid duplicate combos, important detail which I forgot
so once we consider candidates, we should only consider candidates that include that candidate and directly after it
so we need some kind of index to keep track of that
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:    # type: ignore
        res = []
        path = []

        def helper(index, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(index, len(candidates)):
                candidate = candidates[i]
                path.append(candidate)
                helper(i, remaining - candidate)
                path.pop()
        
        
        helper(0, target)
        return res