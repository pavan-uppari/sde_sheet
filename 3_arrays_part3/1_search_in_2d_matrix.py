class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return self.binary_search(row, target)
        return False

    def binary_search(self, row, target) -> bool:
        n = len(row)
        low, high = 0, n-1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return False


"""
Approach2 ->
Do binary search on entire matrix, Trick Formula -> from mid integer, row and column are mid//m and mid%m.

Time Complexity -> O(logn + logm)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        low, high = 0, m*n - 1
        while low <= high:
            mid = (low + high) // 2
            r,c = mid//m, mid%m
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


            