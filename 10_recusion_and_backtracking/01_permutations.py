class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.n = len(nums)
        self.res = []
        self.helper()
        return self.res

    def helper(self, seen=set(), curr=[]):
        if len(seen) == self.n:
            self.res.append(curr[:])
            return

        for ind in range(self.n):
            if ind not in seen:
                seen.add(ind)
                curr.append(self.nums[ind])
                self.helper()
                seen.remove(ind)
                curr.pop()
