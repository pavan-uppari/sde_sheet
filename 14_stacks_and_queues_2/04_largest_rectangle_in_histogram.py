class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        nse_arr = self.nse(heights)
        pse_arr = self.pse(heights)

        res = 0
        for i in range(len(heights)):
            res = max(res, heights[i] * (nse_arr[i] - pse_arr[i] - 1))
        return res

    def nse(self, heights):
        res = []
        stack = []
        for ind in range(len(heights) - 1, -1, -1):
            height = heights[ind]

            while stack and heights[stack[-1]] >= height:
                stack.pop()
            res.append(stack[-1] if stack else len(heights))
            stack.append(ind)

        return res[::-1]

    def pse(self, heights):
        res = []
        stack = []
        for ind, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(ind)

        return res
