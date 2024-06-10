class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = curr = None
        remainder = curr_sum = 0
        while l1 or l2:
            curr_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + remainder
            remainder = curr_sum // 10

            new_node = ListNode(val=curr_sum%10)

            if curr is None:
                res = new_node
                curr = new_node
            else:
                curr.next = new_node
                curr = curr.next
            if l1: 
                l1=l1.next
            if l2: 
                l2=l2.next
        if remainder:
            curr.next = ListNode(val=remainder)

        return res
        