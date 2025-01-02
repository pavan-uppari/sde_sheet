class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        queue = []
        bad_oranges = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    bad_oranges += 1
                    queue.append((i, j))

        res = -1

        while queue:
            for _ in range(len(queue)):
                curr_i, curr_j = queue.pop(0)
                for i, j in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
                    if (
                        self.is_valid(curr_i + i, curr_j + j, n, m)
                        and grid[curr_i + i][curr_j + j] == 1
                    ):
                        grid[curr_i + i][curr_j + j] = 2
                        queue.append((curr_i + i, curr_j + j))

            res += 1

        for item in grid:
            if 1 in item:
                return -1

        if bad_oranges == 0:
            return 0

        return res

    def is_valid(self, i, j, n, m):
        return (0 <= i < n) and (0 <= j < m)
