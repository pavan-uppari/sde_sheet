class Solution:
    def aggressiveCows(self, nums, k):

        self.nums = sorted(nums)
        self.k = k 
        self.n = len(nums)
        self.res = 0
        self.helper()
        return self.res

    def helper(self):

        low, high = 0, self.nums[-1] - self.nums[0]

        while low <= high:

            mid = (low + high) // 2

            if self._is_possible(mid):
                self.res = max(self.res, mid)
                low = mid + 1
            else:
                high = mid - 1

    def _is_possible(self, d):

        prev = 0
        count = self.k - 1

        for i in range(1, self.n):
            if self.nums[i] - self.nums[prev] >= d:
                prev = i
                count -= 1

            if not count:
                return True

        return not count

        