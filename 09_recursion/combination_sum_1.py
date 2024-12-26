class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.res = []
        self.candidates = candidates
        self.n = len(candidates)
        self.target = target
        self.helper()
        return self.res

    def helper(self, ind=0, curr=[], curr_sum=0):

        if curr_sum == self.target:
            self.res.append(curr[:])
            return

        if ind == self.n or curr_sum > self.target:
            return

        curr.append(self.candidates[ind])
        self.helper(ind, curr, curr_sum+self.candidates[ind])

        curr.pop()
        self.helper(ind+1, curr, curr_sum)
        