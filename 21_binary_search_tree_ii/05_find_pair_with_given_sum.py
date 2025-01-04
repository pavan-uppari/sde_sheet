class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.k = k
        return self.helper(root, set())

    def helper(self, node, seen):
        if not node:
            return False

        if self.k - node.val in seen:
            return True

        seen.add(node.val)
        return self.helper(node.left, seen) or self.helper(node.right, seen)
