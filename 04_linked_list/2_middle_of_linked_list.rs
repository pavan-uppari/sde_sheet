impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let (mut slow, mut fast) = (&head, &head);
        loop {
            if let Some(node) = fast {
                fast = &node.next
            } else {
                return slow.clone();
            }
            if let Some(node) = fast {
                fast = &node.next
            } else {
                return slow.clone();
            }
            if let Some(node) = slow {
                slow = &node.next
            }
        }
    }
}
