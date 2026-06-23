from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def dfs(i):
            if i >= len(s):
                res.append(path.copy())
            
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    path.append(s[i: j + 1])
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return res