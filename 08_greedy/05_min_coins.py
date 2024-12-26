class Solution:
    def minCoins(self, V):
        coins = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
        res = 0

        for coin in coins:
            while V and coin <= V:
                res += 1
                V -= coin

        return res
