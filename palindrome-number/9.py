"""Given an integer x, return true if x is a palindrome, and false otherwise.

use 2 pointers and start from opposite ends
l = 0
r = len(x) - 1
keep checking if they're equal
condition for while loop -> while l < r
because eventually they will cross
ex: 3 digit number, l and r will meet at the same position, index 1

-2^31 <= x <= 2^31 - 1"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
