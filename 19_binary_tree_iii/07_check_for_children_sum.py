class Solution:
    def isSumProperty(self, root):
        if not root:
            return 1
        if root.left is None and root.right is None:
            return 1

        left = root.left.data if root.left else 0
        right = root.right.data if root.right else 0

        return (
            (1 if root.data == left + right else 0)
            and self.isSumProperty(root.left)
            and self.isSumProperty(root.right)
        )
