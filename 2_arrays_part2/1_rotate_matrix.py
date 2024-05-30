#Using extra memory approach
def method(matrix):
    """
    logic - i,j = j,n-i-1
    """

    n = len(matrix)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n-i-1] = matrix[i][j]
    return res

#Better approach without using extra memory
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        1. Transpose the matrix
        2. Reverse each row
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        return matrix
        