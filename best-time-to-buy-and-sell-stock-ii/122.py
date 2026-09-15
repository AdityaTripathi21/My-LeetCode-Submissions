"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

prices = [7, 1, 5, 3, 6, 4]
buy day 2, price = 1, sell day 3, price = 5, profit = 5 - 1 = 4. buy day 4, price = 3, sell day 5, price = 6,
profit = 6 - 3 = 3, total profit = 3 + 4 = 7

always make the greedy choice. Why? because you can keep buying and selling, so if a price is greater than the price before it, always sell. 
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:  # type: ignore
        total = 0
        for i in range(1, len(prices)):
            total += max(0, prices[i] - prices[i - 1])
        return total    
        