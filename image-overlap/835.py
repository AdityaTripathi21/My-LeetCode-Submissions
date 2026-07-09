from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # given a coordinate shift, count the number of 1s
        def helper(y_shift, x_shift):
            count = 0
            for r in range(n):
                for c in range(n):
                    if (0 <= r + y_shift < n and 0 <= c + x_shift < n and 
                    img1[r][c] == 1 and img2[r+y_shift][c+x_shift] == 1):
                        count += 1
            return count
        
        res = []
        for r in range(-n + 1, n):
            for c in range(-n + 1, n):
                res.append(helper(r, c))
        return max(res)