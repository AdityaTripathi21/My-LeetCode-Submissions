"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4

recurrence relation => dp[i] where dp[i] represents the min amount of coins to make amount i
the min amount of coins isn't made from a greedy algorithm
dp[i] = min(dp[i-x]) + 1 for x in coins
base case -> dp[0] = 0
dp[i] starts at infinity because we don't know if we can make these amounts yet
if dp[n] is still inf at the end, that means we can't make that amount, return -1"""



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # type: ignore
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]   # type: ignore
                
        