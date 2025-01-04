class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return 0

        lh = self.helper(node.left)
        rh = self.helper(node.right)

        if abs(lh - rh) > 1:
            self.res = False

        return 1 + max(lh, rh)
