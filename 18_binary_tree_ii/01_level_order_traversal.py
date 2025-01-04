class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = [root]
        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(curr)
        return res
