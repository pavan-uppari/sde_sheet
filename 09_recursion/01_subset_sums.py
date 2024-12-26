class Solution:
    def subsetSums(self, arr):
        self.res = []
        self.arr = arr
        self.n = len(arr)
        self.helper()
        return self.res

    def helper(self, ind=0, curr=0):
        if ind == self.n:
            self.res.append(curr)
            return

        self.helper(ind + 1, curr + self.arr[ind])
        self.helper(ind + 1, curr)
