class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        val, wt = zip(*sorted(zip(val, wt), key=lambda x: x[0] / x[1], reverse=True))
        res = 0

        for a, b in zip(val, wt):
            if b <= capacity:
                res += a
                capacity -= b
            else:
                res += (a / b) * capacity
                break
        return res
