class Solution:
    def floor(self, root, X):
        node = root
        res = -1

        while node:
            if node.data == X:
                return node.data
            elif node.data < X:
                res = max(res, node.data)
                node = node.right
            else:
                node = node.left

        return res
