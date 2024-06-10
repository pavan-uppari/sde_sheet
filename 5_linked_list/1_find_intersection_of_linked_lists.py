class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        l1 = self.get_length_of_linked_list(headA)
        l2 = self.get_length_of_linked_list(headB)

        curr1 = headA
        curr2 = headB
        if l1>l2:
            for _ in range(l1 - l2): curr1 = curr1.next
        else:
            for _ in range(l2 - l1): curr2 = curr2.next
        while curr1 and curr2:
            if curr1 == curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next
        return None

    def get_length_of_linked_list(self, node: ListNode):
        res = 0
        while node:
            res += 1
            node = node.next
        return res


#TODO need to check optimal approach

        