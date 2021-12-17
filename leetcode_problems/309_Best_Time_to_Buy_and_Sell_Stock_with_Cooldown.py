from functools import lru_cache
## problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
## discussion https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/1522708/Python-3-Bottom-up-DP-%2B-memoization-O(n)-time-and-space-code-%2B-comments

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
"""


class Solution:
    def maxProfit(self, prices: list) -> int:

        # Bottom-up dynamic programming with memoization (caching)
        @lru_cache(None)
        def dp(day: int, can_buy: True) -> int:

            # Base case
            if day >= len(prices):
                return 0

            if can_buy:
                # We don't own any stocks. Two options:
                # 1. Don't buy any stocks and go to the next day (wait for a better opportunity)
                # 2. Buy stocks and go to the next day (with hope to have the best profit)
                return max(dp(day + 1, True), dp(day + 1, False) - prices[day])
            else:
                # We own stocks. Two options:
                # 1. Don't sell any stocks and go to the next day (maybe there is a better selling price)
                # 2. Sell the stocks and go to the day after tomorrow (cooldown tomorrow)
                return max(dp(day + 1, False), dp(day + 2, True) + prices[day])

        # Start with no stocks
        return dp(0, True)

prices = [1,2,3,0,2]

s = Solution()
print(s.maxProfit(prices))