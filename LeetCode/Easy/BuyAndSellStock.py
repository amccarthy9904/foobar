# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock
# Easy
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Runtime 751ms Beats 69.98% of users with Python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, diff = 0, 0
        

        for r in range(1, len(prices)):

            if prices[l] >= prices[r]:
                l = r
            else:
                diff = max(diff, prices[r] - prices[l])
        
        return diff

        