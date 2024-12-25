class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
