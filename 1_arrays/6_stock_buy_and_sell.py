"""
https://takeuforward.org/data-structure/stock-buy-and-sell/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#easy
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==1:
            return 0
        result = 0
        curr_mini = prices[0]
        for item in prices[1:]:
            curr_mini = min(curr_mini, item)
            result = max(result, item - curr_mini)
        return result
        