class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        result = 0
        curr_mini = prices[0]
        for item in prices[1:]:
            curr_mini = min(curr_mini, item)
            result = max(result, item - curr_mini)
        return result
