class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        stack = []

        for num in nums2[::-1]:
            while stack and stack[-1] <= num:
                stack.pop()

            nge[num] = stack[-1] if stack else -1
            stack.append(num)

        return [nge[num] for num in nums1]
