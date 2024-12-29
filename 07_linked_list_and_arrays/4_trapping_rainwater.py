class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)

        pre_max = []
        suff_max = []

        curr_pre_max = curr_suff_max = 0

        for i in range(n):
            curr_pre_max = max(curr_pre_max, heights[i])
            pre_max.append(curr_pre_max)

            curr_suff_max = max(curr_suff_max, heights[n - i - 1])
            suff_max.insert(0, curr_suff_max)

        res = 0
        for a, b, c in zip(heights, pre_max, suff_max):
            res += min(b, c) - a

        return res
