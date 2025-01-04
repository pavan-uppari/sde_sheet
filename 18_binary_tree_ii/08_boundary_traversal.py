class Solution:
    def traverseBoundary(self, root):
        # edge case: if root is leaf node
        if root.left is None and root.right is None:
            return [root.data]

        return (
            [root.data]
            + self.get_left_boundary(root.left)
            + self.get_leaves(root)
            + self.get_right_boundary(root.right)[::-1]
        )

    def get_left_boundary(self, node):
        res = []

        while node:
            if not (node.left is None and node.right is None):
                res.append(node.data)

            if node.left:
                node = node.left
            else:
                node = node.right

        return res

    def get_right_boundary(self, node):
        res = []

        while node:
            if not (node.left is None and node.right is None):
                res.append(node.data)

            if node.right:
                node = node.right
            else:
                node = node.left

        return res

    def get_leaves(self, node, leaves=[]):
        if node.left is None and node.right is None:
            leaves.append(node.data)

        if node.left:
            self.get_leaves(node.left)

        if node.right:
            self.get_leaves(node.right)

        return leaves
