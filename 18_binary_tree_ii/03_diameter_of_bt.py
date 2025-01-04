class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return 0

        lh = self.helper(node.left)
        rh = self.helper(node.right)

        self.res = max(self.res, lh + rh)

        return 1 + max(lh, rh)
