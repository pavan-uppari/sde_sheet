class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = curr = 0
        for i,v in enumerate(nums):
            if v == 1:
                curr+=1
            else:
                res = max(res, curr)
                curr = 0
        return max(curr, res)