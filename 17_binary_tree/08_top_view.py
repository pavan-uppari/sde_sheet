class Solution:
    def topView(self, root):
        if not root:
            return []

        view = {}
        queue = [(root, 0)]

        while queue:
            node, level = queue.pop(0)

            if level not in view:
                view[level] = node.data

            if node.left:
                queue.append((node.left, level - 1))
            if node.right:
                queue.append((node.right, level + 1))

        return [view[key] for key in sorted(view)]
