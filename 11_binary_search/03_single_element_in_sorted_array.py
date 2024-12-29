class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        low, high = 1, n - 2

        while low <= high:
            mid = (low + high) // 2

            if nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]

            elif nums[mid] == nums[mid - 1]:
                if mid % 2:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if mid % 2:
                    high = mid - 1
                else:
                    low = mid + 1
