from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # dp[i]
        dp[len(s)] = True   # base case, dp[len(s)] is empty string

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]