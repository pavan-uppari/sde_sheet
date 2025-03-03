class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.s = s
        self.n = len(s)
        self.helper()
        return self.res

    def helper(self, ind=0, curr=[]):
        if ind == self.n:
            self.res.append(curr[:])
            return

        for i in range(ind, self.n):
            curr_string = self.s[ind : i + 1]
            if curr_string == curr_string[::-1]:
                curr.append(curr_string)
                self.helper(i + 1, curr)
                curr.pop()
