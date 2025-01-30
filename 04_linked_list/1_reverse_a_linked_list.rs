impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev: Option<Box<ListNode>> = None;
        let mut curr = head;

        while let Some(mut node) = curr {
            let nextnode = node.next;
            node.next = prev;
            prev = Some(node);
            curr = nextnode;
        }

        prev
    }
}