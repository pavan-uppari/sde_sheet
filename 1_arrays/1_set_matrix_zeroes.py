"""
https://takeuforward.org/data-structure/set-matrix-zero/
https://leetcode.com/problems/set-matrix-zeroes/

#medium

Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        1. First find the indexes of rows and columns where 0 is present
        2. Iterate through matrix again to make relevant items to zero
        """
        r: set[int] = set()
        c: set[int] = set()
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        for i in range(m):
            for j in range(n):
                if (i in r) or (j in c):
                    matrix[i][j] = 0
