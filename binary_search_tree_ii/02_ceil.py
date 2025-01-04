class Solution:
    def findCeil(self, root, X):
        res = float("inf")
        node = root

        while node:
            if node.key == X:
                return node.key

            elif node.key > X:
                res = min(res, node.key)
                node = node.left

            else:
                node = node.right

        return res if res != float("inf") else -1
