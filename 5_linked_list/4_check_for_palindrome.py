class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        curr1 = head
        curr2 = prev
        while curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return True
        