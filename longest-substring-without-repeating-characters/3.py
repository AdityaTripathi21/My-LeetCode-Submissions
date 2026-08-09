"""Given a string s, find the length of the longest substring without duplicate characters.

0 <= s.length <= 10^5 -> small/mediumish
s consists of English letters, digits, symbols and spaces.

s = "abcabcbb"
res = 3, abc, bca, cab

s = "bbbbb"
res = 1, any b

s = "pwwkew"
res = 3, wke
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

obviously need sliding window of variable size -> need 2 pointers to maintain window
need to keep track of character frequency within the map
frequency of all characters must be 1
so we need hashmap to keep track of char freq
the hashmap keeps track of freq of the window
if a character ends up with a freq of 2, we move the left pointer, or actually idk
abcab -> 
a: 1
a: 1, b : 1
a: 1, b : 1, c : 1
a : 2, b : 1, c: 1
just move left pointer till freq is back to 1 """

"""
I manually processed the first element for this solution,
for these types of problems, I need to ask myself if the loop can handle
every element and this helps make the code cleaner and makes edge cases easier to handle
"""




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq_map = {} # key: value = letter: count in current window

        l = 0
        r = 0

        res = 1
        curr = 0

        if len(s) == 0:
            return 0

        freq_map[s[l]] = 1

        for r in range(len(s) - 1):
            r += 1

            freq_map[s[r]] = freq_map.get(s[r], 0) + 1

            while freq_map[s[r]] > 1:
                freq_map[s[l]] -= 1
                l += 1

            curr = r - l + 1
            
            res = max(res, curr)
        
        return res
