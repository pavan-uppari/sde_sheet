class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = set()
        self.candidates = sorted(candidates)
        self.n = len(candidates)
        self.target = target
        self.helper()
        return list(self.res)

    def helper(self, ind=0, curr=[], curr_sum=0):

        if curr_sum == self.target:
            self.res.add(tuple(curr[:]))
            return

        if ind == self.n or curr_sum > self.target:
            return

        curr.append(self.candidates[ind])
        self.helper(ind+1, curr, curr_sum+self.candidates[ind])

        curr.pop()
        for i in range(ind+1, self.n):
            if self.candidates[i] != self.candidates[ind]:
                self.helper(i, curr, curr_sum)
                break
        
        