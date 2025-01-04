class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        curr_level_head = root

        while curr_level_head and curr_level_head.left:
            temp = curr_level_head

            while temp:
                temp.left.next = temp.right
                if temp.next:
                    temp.right.next = temp.next.left
                temp = temp.next

            curr_level_head = curr_level_head.left

        return root
