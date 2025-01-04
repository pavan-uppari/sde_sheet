class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)

    def helper(self, left_node, right_node):
        if left_node is None:
            return right_node is None

        if right_node is None:
            return left_node is None

        return (
            left_node.val == right_node.val
            and self.helper(left_node.left, right_node.right)
            and self.helper(left_node.right, right_node.left)
        )
