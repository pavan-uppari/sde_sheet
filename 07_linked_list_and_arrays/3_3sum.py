class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                required_num = 0 - nums[i] - nums[j]
                if required_num in seen:
                    res.add((nums[i], nums[j], required_num))
                seen.add(nums[j])
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if not curr_sum:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res
