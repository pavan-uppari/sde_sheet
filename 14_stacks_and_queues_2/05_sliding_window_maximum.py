class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = []
        n = len(nums)
        res = []

        for ind, num in enumerate(nums):
            if deque and deque[0] <= ind - k:
                deque.pop(0)

            while deque and nums[deque[-1]] < num:
                deque.pop()

            deque.append(ind)

            if ind >= k - 1:
                res.append(nums[deque[0]])

        return res
