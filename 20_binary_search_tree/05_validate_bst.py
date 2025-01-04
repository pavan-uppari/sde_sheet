class Solution:
    def isValidBST(
        self, root: Optional[TreeNode], mini=float("-inf"), maxi=float("inf")
    ) -> bool:
        if not root:
            return True

        if not (mini < root.val < maxi):
            return False

        return self.isValidBST(root.left, mini, root.val) and self.isValidBST(
            root.right, root.val, maxi
        )
