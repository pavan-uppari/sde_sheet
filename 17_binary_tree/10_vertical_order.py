from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        view = defaultdict(list)
        queue = [(root, 0)]

        while queue:
            curr_view = defaultdict(list)

            for _ in range(len(queue)):
                node, level = queue.pop(0)
                curr_view[level].append(node.val)

                if node.left:
                    queue.append((node.left, level - 1))
                if node.right:
                    queue.append((node.right, level + 1))

            for level in curr_view:
                if level in view:
                    view[level].extend(sorted(curr_view[level]))
                else:
                    view[level] = sorted(curr_view[level])

        return [view[key] for key in sorted(view)]
