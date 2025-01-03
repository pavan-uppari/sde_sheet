class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.inorder(root)
        return self.res

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.res.append(node.val)
        self.inorder(node.right)
