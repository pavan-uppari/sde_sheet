class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.preorder(root)
        return self.res

    def preorder(self, node):
        if not node:
            return

        self.res.append(node.val)
        self.preorder(node.left)
        self.preorder(node.right)
