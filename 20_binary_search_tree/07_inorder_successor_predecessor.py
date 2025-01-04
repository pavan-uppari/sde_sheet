class Solution:
    def succPredBST(self, root, key):
        pred = succ = -1

        self.key = key

        curr = root

        while curr:
            if curr.data < key:
                pred = curr.data
                curr = curr.right
            else:
                curr = curr.left

        curr = root
        while curr:
            if curr.data > key:
                succ = curr.data
                curr = curr.left
            else:
                curr = curr.right

        return pred, succ
