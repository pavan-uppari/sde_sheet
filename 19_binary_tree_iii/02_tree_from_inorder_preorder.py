class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return

        root_val = preorder.pop(0)
        node = TreeNode(root_val)

        root_inorder_ind = inorder.index(root_val)

        node.left = self.buildTree(
            preorder[:root_inorder_ind], inorder[:root_inorder_ind]
        )
        node.right = self.buildTree(
            preorder[root_inorder_ind:], inorder[root_inorder_ind + 1 :]
        )

        return node
