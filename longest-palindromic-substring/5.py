class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_res = r_res = 0
        for i in range(len(s)):
            # odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > (r_res - l_res + 1):
                    l_res = l
                    r_res = r
                l -= 1
                r += 1
            
            # even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > (r_res - l_res + 1):
                    l_res = l
                    r_res = r
                l -= 1
                r += 1
        return s[l_res:r_res + 1]
