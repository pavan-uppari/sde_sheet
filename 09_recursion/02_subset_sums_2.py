class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = set()
        self.nums = nums
        self.n = len(nums)
        self.helper()
        return list(self.res)

    def helper(self, ind=0, curr=[]):
        if ind == self.n:
            self.res.add(tuple(sorted(curr)))
            return

        curr.append(self.nums[ind])
        self.helper(ind + 1, curr)

        curr.pop()
        self.helper(ind + 1, curr)
