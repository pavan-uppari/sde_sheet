class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.b = board
        self.helper()

    def helper(self):
        for i in range(9):
            for j in range(9):
                if self.b[i][j] == ".":
                    for digit in "123456789":
                        if self.is_valid(i, j, digit):
                            self.b[i][j] = digit
                            if self.helper():
                                return True
                            self.b[i][j] = "."
                    return False

        return True

    def is_valid(self, row, col, digit):
        for i in range(9):
            for j in range(9):
                if self.b[i][col] == digit or self.b[row][j] == digit:
                    return False

        grid_row, grid_col = (row // 3) * 3, (col // 3) * 3
        for i in range(grid_row, grid_row + 3):
            for j in range(grid_col, grid_col + 3):
                if self.b[i][j] == digit:
                    return False

        return True
