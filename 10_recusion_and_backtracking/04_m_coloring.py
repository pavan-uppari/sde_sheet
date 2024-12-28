from collections import defaultdict


class Solution:
    def graphColoring(self, edges, m, n):
        self.adj = defaultdict(list)

        for edge in edges:
            self.adj[edge[0]].append(edge[1])
            self.adj[edge[1]].append(edge[0])

        self.m = m
        self.n = n
        return self.helper()

    def helper(self, curr_node=0, colored={}):
        if curr_node == self.n:
            return True

        for color in range(self.m):
            if self.is_valid(curr_node, colored, color):
                colored[curr_node] = color
                if self.helper(curr_node + 1):
                    return True

        return False

    def is_valid(self, node, colored, color) -> bool:
        for adj_node in self.adj[node]:
            if colored.get(adj_node) == color:
                return False

        return True
