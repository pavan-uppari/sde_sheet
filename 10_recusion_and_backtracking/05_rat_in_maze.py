class Solution:
    def findPath(self, mat):
        self.mat = mat
        self.n = len(mat)
        self.res = []
        self.helper()
        return sorted(self.res)

    def helper(self, r=0, c=0, curr="", seen=set()):
        if not self.is_valid(r, c, seen):
            return

        if r == self.n - 1 and c == self.n - 1:
            self.res.append(curr)
            return

        seen.add((r, c))
        self.helper(r + 1, c, curr + "D")
        self.helper(r - 1, c, curr + "U")
        self.helper(r, c + 1, curr + "R")
        self.helper(r, c - 1, curr + "L")
        seen.remove((r, c))

    def is_valid(self, r, c, seen):
        return not (
            r < 0
            or c < 0
            or r >= self.n
            or c >= self.n
            or (r, c) in seen
            or not self.mat[r][c]
        )
