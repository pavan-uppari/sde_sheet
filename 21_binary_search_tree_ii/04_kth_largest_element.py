class Solution:
    def kthLargest(self, root, k):
        self.k = k
        self.res = None
        self.inorder(root)
        return self.res

    def inorder(self, node):
        if not node:
            return

        self.inorder(node.right)
        self.k -= 1
        if not self.k:
            self.res = node.data
            return
        self.inorder(node.left)
