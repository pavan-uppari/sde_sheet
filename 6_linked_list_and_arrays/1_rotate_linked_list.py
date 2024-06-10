class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        n = 0
        curr = head
        while curr:
            n+=1
            curr = curr.next

        k = (k % n) if n else 0
        if k == 0: return head

        fast = head
        for _ in range(k): fast = fast.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        res = slow.next
        fast.next = head
        slow.next = None
        return res
