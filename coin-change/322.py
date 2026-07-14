from cmath import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        
        dp[0] = 0

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= curr_amount:
                    dp[curr_amount] = min(
                        dp[curr_amount],
                        dp[curr_amount - coin] + 1
                    )
        
        return -1 if dp[amount] == inf else dp[amount] # type: ignore