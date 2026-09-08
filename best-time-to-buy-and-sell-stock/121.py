"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

1 <= prices.length <= 10^5  -> medium
0 <= prices[i] <= 10^4  -> medium

arr length can be 1, which means you must return 0, so potential base case

obviously need 2 pointers
if you see a new potential min value, you must pick it
let's say you have [7, 2, 1, 5], your min will be 7, then 2, and then you must 1, because when you see 5, 5 - 1 = 4 > 5 - 2 = 3. So if you find a new min, that means the max will also have to be reset, because the max must come after

so in this case: [7, 2, 6, 1, 3] -> you'll pick 1 as new min, and then new max will be 3, but 3 - 1 = 2 which is less than 6 - 2 = 4, so make sure to save current best. need variable for that as well

you only need to keep track of the current min and not current max because you can treat each day as a potential 
selling day, so then you only need cur min and best, also for my approach, this invariant needs to be maintained always: cur_max >= cur_min

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:  # type: ignore
        if len(prices) == 1:
            return 0
        
        best = 0
        cur_min = 0
        cur_max = 1

        for i in range(1, len(prices)):

            if prices[i] < prices[cur_min]:
                cur_min = i
                cur_max = i
            elif prices[i] > prices[cur_max]:
                cur_max = i
            
            best = max(best, prices[cur_max] - prices[cur_min])

        
        return best


            
