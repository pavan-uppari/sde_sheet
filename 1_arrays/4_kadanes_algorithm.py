"""
https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/
https://leetcode.com/problems/maximum-subarray/submissions/1269379519/
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum

#easy
"""

#TODO Print actual sub array as follow up question


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxi_sum = nums[0]
        curr_sum = nums[0]
        for item in nums[1:]:
            curr_sum = max(item, curr_sum + item)
            maxi_sum = max(maxi_sum, curr_sum)
        return maxi_sum
        