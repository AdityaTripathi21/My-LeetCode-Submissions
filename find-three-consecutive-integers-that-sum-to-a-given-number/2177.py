"""Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.

0 <= num <= 10^15 -> huge

just check all integers up to like n/3
because (n/3) + (n/3) + 1 + (n/3) + 2 = n + 3, so this is greater than n, but just check until to be safe cuz why not, as soon as you find a solution that works, just return it

actually, you can think of numbers as x - 1, x, x + 1, so solutions must sum up to 3x, so you just have to find that value for x, so 3x = n, => x = n/3, so jus check if that exists, very simple"""

class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3 == 0:
            x = num//3
            return [x - 1, x, x + 1]
        return []