class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return 0

        ls = max(0, self.helper(node.left))
        rs = max(0, self.helper(node.right))

        self.res = max(self.res, node.val + ls + rs)

        return node.val + max(ls, rs)
