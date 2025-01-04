class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        self.inorder(root)
        return self.res

    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)
        self.k -= 1
        if not self.k:
            self.res = node.val
            return
        self.inorder(node.right)
