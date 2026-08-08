"""Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

1 <= s.length <= 10^5 -> small/mediumish
s consists of lowercase English letters.
1 <= k <= s.length

s = "abciiidef", k = 3
abc -> 1
bci -> 1
cii -> 2
iii - > 3
iid -> 2
ide -> 2
def -> 1
use 2 pointers for sliding window
stop when right pointer = len(s)

to avoid recomputing string every time, just add one to the window and subtract one constantly
rebuilding the substring each time costs O(k) and over n steps, that's O(nk)
however just checking if vowels 
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = k

        res = 0
        cur = 0

        vowels = set("aeiou")

        for w in s[l:k]:
            if w in vowels:
                res += 1
        
        cur = res

        while r < len(s):
            if s[l] in vowels:
                cur -= 1
            
            if s[r] in vowels:
                cur += 1
            
            l += 1
            r += 1

            res = max(res, cur)

        return res




