class Solution:
    def wordBreak(self, s, dictionary):
        self.s = s
        self.n = len(s)
        self.words = set(dictionary)
        self.res = []
        self.helper()
        return self.res

    def helper(self, curr_ind=0, curr=[]):
        if curr_ind == self.n:
            self.res.append(curr[:])
            return

        for i in range(curr_ind, self.n):
            if self.s[curr_ind : i + 1] in self.words:
                curr.append(self.s[curr_ind : i + 1])
                self.helper(i + 1)
                curr.pop()
