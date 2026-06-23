from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        num_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []
        path = []

        def dfs(i):
            if len(path) == len(digits):
                res.append("".join(path.copy()))
                return
            
            for char in num_map[digits[i]]:
                path.append(char)
                dfs(i + 1)
                path.pop()


            

        dfs(0)
        return res