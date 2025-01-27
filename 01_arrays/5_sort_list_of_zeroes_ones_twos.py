class Solution:
    def sortColors(self, nums: List[int]) -> None:
        li = 0
        ri = len(nums) - 1

        curr = li
        while curr <= ri:
            if nums[curr] == 0:
                nums[curr], nums[li] = nums[li], nums[curr]
                li += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[ri] = nums[ri], nums[curr]
                ri -= 1
            elif nums[curr] == 1:
                curr += 1
