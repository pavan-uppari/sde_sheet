from collections import defaultdict


class Solution:
    def celebrity(self, M):
        i_know = defaultdict(int)
        know_me = defaultdict(int)

        n = len(M)
        m = len(M[0])

        for i in range(n):
            for j in range(m):
                if M[i][j]:
                    i_know[i] += 1
                    know_me[j] += 1

        for i in range(n):
            if i_know[i] == 0 and know_me[i] == n - 1:
                return i

        return -1
