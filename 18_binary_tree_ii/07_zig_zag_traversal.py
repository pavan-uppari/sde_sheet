class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = [root]
        zig_zag = 1

        while queue:
            curr_level = []

            for _ in range(len(queue)):
                curr_node = queue.pop(0)

                curr_level.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            res.append(curr_level[::zig_zag])
            zig_zag *= -1

        return res
