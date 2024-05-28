"""
https://takeuforward.org/data-structure/find-the-majority-element-that-occurs-more-than-n-2-times/
https://leetcode.com/problems/majority-element/

#easy
"""


# Cancelling out if count if zero. If it is majority element, count won't become zero (won't be cancelled out)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                curr = num
                count = 1
            elif num == curr:
                count+=1
            else:
                count -=1
        return curr
        