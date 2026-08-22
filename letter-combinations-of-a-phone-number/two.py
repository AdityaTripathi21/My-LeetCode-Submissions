"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

1 <= digits.length <= 4 -> very small
digits[i] is a digit in the range ['2', '9'].

need map for digits, so k: v -> str -> list[str]

problem asks for all possible combos and small input length -> backtracking

for every digit, we can choose a letter, and then choose the next position
after we have chosen all digits, we backtrack and then try the next letter

hold all combinations in a list[str] called res
current path will be a string called path


choices -> Choose any letter mapped to the digit at the current position.
constraints -> none
base case -> all positions are filled or current path length is equal to length of digits
backtracking -> choose letter, add to path, recurse from the next digit, remove letter from path"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]: # type: ignore
        res = []
        path = ""

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def helper(path):
            if len(path) == len(digits):
                res.append(path)
                return
            
            cur_pos = len(path)
            cur_digit = digits[cur_pos]

            for letter in digit_to_letters[cur_digit]:
                helper(path + letter)
        
        helper("")
        return res
                

        