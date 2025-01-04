class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.postorder(root)
        return self.res

    def postorder(self, node):
        if not node:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        self.res.append(node.val)
