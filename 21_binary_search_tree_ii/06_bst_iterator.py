class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.inorder_arr = []
        self._inorder(root)
        self.curr_ind = -1

    def next(self) -> int:
        self.curr_ind += 1
        return self.inorder_arr[self.curr_ind]

    def hasNext(self) -> bool:
        return (self.curr_ind + 1) < len(self.inorder_arr)

    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        self.inorder_arr.append(node.val)
        self._inorder(node.right)
