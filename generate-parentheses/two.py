"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

1 <= n <= 8 -> small input -> large TC

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

what is well formed parentheses? -> every open parenthesis must be closed, and no closed parenthesis must come before open parenthesis

for n = 3, we need 3 opens, and 3 closes, and they have to satisfy the rules outlined above

you will always start out with an open, and then you keep adding opens as long as open is less than n, 
you can only add closes if closes are less than open

you return when the string is equal to 2 * n in length
note: we know the current path will always be valid because it has to satisfy the conditions outlined above

choices -> open or close
constraints -> add open if open < n, add close if close < open
base case -> len(path) == 2 * n
backtracking -> add open or close to path, recurse, pop it off and explore other choices"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]: # type: ignore
        res = []

        def helper(open, close, path):
            if len(path) == 2 * n:
                res.append(path)
                return 

            if open < n:
                helper(open + 1, close, path + "(")

            if close < open:
                helper(open, close + 1, path + ")")        

        helper(0, 0, "")
        return res