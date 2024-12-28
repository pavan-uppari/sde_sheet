class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.n = n
        board = [["."] * n for _ in range(n)]
        self.helper(board)
        return self.res

    def helper(self, board, ind=0):
        if ind == self.n:
            self.res.append(["".join(item) for item in board])
            return

        for i in range(self.n):
            if self.is_valid(ind, i, board):
                board[ind][i] = "Q"
                self.helper(board, ind + 1)
                board[ind][i] = "."

    def is_valid(self, row, col, board) -> bool:
        # up
        r = row - 1
        while r >= 0:
            if board[r][col] == "Q":
                return False
            r -= 1

        # left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # up diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < self.n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True
