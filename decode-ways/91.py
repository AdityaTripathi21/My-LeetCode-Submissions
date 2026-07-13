class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]

            if i >= len(s):
                return 1
            elif s[i] == "0":
                return 0
            
            ways = dp(i + 1)

            
            if i < len(s) - 1 and int(s[i:i+2]) <= 26:
                ways += dp(i + 2)
            memo[i] = ways
            return ways
        return dp(0)