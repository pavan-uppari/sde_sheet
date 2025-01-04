class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return

        root_val = postorder.pop()
        node = TreeNode(root_val)

        root_inorder_ind = inorder.index(root_val)

        node.left = self.buildTree(
            inorder[:root_inorder_ind], postorder[:root_inorder_ind]
        )
        node.right = self.buildTree(
            inorder[root_inorder_ind + 1 :], postorder[root_inorder_ind:]
        )

        return node
