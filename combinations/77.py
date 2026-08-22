"""Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

1 <= n <= 20
1 <= k <= n

small constraints => large TC

combinations -> order doesn't matter, [1,2] is the same thing as [2,1]

use backtracking -> why? -> asking to generate all combinations

instead of going by index, go by position that needs to be filled
when len(path) == k, add path to res and return

loop over all elements, also need to keep track of visited elements, so use set
how to prevent duplicate combos? If I already have [1,2], how do I prevent [2,1]?
maybe use double loop, so once I get to 2, start from 3 and not 1 again

since you start loops from next element, don't need set for visited
because every single element visited will be unique

choices -> choose any number from starting number to n
constraints -> Every chosen number must come after the previous chosen number.
base case -> if len(path) == k, return
backtracking -> add number, recurse after that number, pop it """

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:   # type: ignore
        res = []
        path = []

        def helper(start, path):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                helper(i + 1, path)
                path.pop()
        
        helper(1, path)
        return res
            



        