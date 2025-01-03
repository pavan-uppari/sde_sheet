class Solution:
    def LeftView(self, root):
        res = []

        if not root:
            return res

        queue = [root]

        while queue:
            res.append(queue[0].data)

            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return res
