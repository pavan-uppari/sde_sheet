# Brute Force
# Time - m!*n!
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        1. If curr indexes crossed the boundary, return 0
        2. If curr indexes are at destination, return 1
        3. Recursively perform the above by increasing the currrent indexes
        """
        return self.helper(0, 0, m, n)

    def helper(self, m1, n1, m, n):
        if m1 >= m or n1 >= n:
            return 0
        if m1 == m - 1 and n1 == n - 1:
            return 1
        return self.helper(m1, n1 + 1, m, n) + self.helper(m1 + 1, n1, m, n)


# Optimal - DP Approach
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Idea is same as above, but the difference is, once you compute the value of a node, store it and use that value if that node is called again
        """
        return self.helper(0, 0, m, n, {})

    def helper(self, m1, n1, m, n, dp):
        if (m1, n1) in dp:
            return dp[(m1, n1)]
        if m1 >= m or n1 >= n:
            return 0
        if m1 == m - 1 and n1 == n - 1:
            return 1
        dp[(m1, n1)] = self.helper(m1, n1 + 1, m, n, dp) + self.helper(
            m1 + 1, n1, m, n, dp
        )
        return dp[(m1, n1)]
