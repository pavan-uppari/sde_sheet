class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n <= 1:
            return n

        res = 1
        curr_count = 1

        prev = nums[0]
        for num in nums[1:]:
            if prev + 1 == num:
                curr_count += 1
                prev = num
            elif num == prev:
                continue
            else:
                prev = num
                res = max(res, curr_count)
                curr_count = 1

        return max(res, curr_count)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        temp = {i: 1 for i in nums}
        for i in nums:
            if i - 1 in temp or i + res not in temp:
                continue
            c = 1
            e = i
            while e + 1 in temp:
                c += 1
                e += 1
            res = max(res, c)
        return res
