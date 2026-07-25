"""
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

1 <= words.length <= 10^5 -> large

words[i].length == 2 -> small

words[i] is only lowercase english letters, example: "cc", "ll", "xx"

 words = ["lc","cl","gg"]
 output = 6
 lc + gg + cl

only palindromes of even length will be created -> 0, 2, 4, 6, ...

if you find a string, you should try to find its reverse, -> cl, lc
look for strings that only contain the same letter -> gg, cc, xx, etc.

maybe create a hashmap to look for reverse? 
we don't even need to create the string, just count it.

create a count variable to keep track of symmetric strings like gg, cc
create a count variable to keep track of asymmetric strings like cl, lc

create map that looks for reverse, so if we're on lc, look for cl, see it hasn't been processed yet
so increment it, and then when we get to cl, check its reverse key which is lc, decrement it, increase count for asymmetric strings

for symmetric strings, there can still be pairs, so make sure to check for that as well

finally, if there are still any positive frequencies remaining, that means this word wasn't matched
so check the map for any positive frequencies and also if that word is equal to its reverse, cause then 
we have a center and can add 2 more to the res, otherwise, don't add anything because you can have still 
have positive frequencies but the word won't be symmetric.


"""



from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq_map = {}

        symm_count = 0
        asymm_count = 0

        for word in words:
            rev = word[::-1]

            if freq_map.get(rev, 0) > 0:
                freq_map[rev] -= 1

                if rev == word:
                    symm_count += 1
                else: 
                    asymm_count += 1
            else:
                freq_map[word] = freq_map.get(word, 0) + 1
        
        res = 4 * (symm_count + asymm_count)

        has_center = any(
            count > 0 and word == word[::-1]
            for word, count in freq_map.items()
        )

        if has_center:
            res += 2
            return res
        return res
        


        