class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        queue = [(root, 0)]

        while queue:
            res = max(res, queue[-1][-1] - queue[0][-1] + 1)

            for _ in range(len(queue)):
                node, index = queue.pop(0)

                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

        return res
