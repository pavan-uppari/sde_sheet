class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow=fast=entry=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                while slow!=entry:
                    slow=slow.next
                    entry=entry.next
                return entry
        return None