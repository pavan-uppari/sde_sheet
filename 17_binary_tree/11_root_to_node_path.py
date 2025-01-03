class Solution:
    def Paths(self, root):
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node, curr=[]):
        if node.left is None and node.right is None:
            curr.append(node.data)
            self.res.append(curr[:])
            curr.pop()
            return

        curr.append(node.data)
        if node.left:
            self.helper(node.left)
        if node.right:
            self.helper(node.right)
        curr.pop()
