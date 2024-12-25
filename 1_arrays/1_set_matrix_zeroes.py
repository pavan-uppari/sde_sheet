class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r: set[int] = set()
        c: set[int] = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        for i in range(m):
            for j in range(n):
                if (i in r) or (j in c):
                    matrix[i][j] = 0
