class Solution:
    def missingNumber(self, nums: list[int]) -> list[int, int]:
        n = len(nums)
        Sn = n * (n + 1) // 2
        S2n = n * (n + 1) * (2 * n + 1) / 6

        my_Sn = my_S2n = 0

        for num in nums:
            my_Sn += num
            my_S2n += num * num

        # equation1 - X+Y = (my_S2n - S2n) / (my_Sn-Sn)

        equation_1_value = (my_S2n - S2n) / (my_Sn - Sn)

        # equation2 - X-Y = my_Sn- Sn
        equation_2_value = my_Sn - Sn

        return [
            (equation_1_value + equation_2_value) // 2,
            (equation_1_value - equation_2_value) // 2,
        ]


obj = Solution()
assert obj.missingNumber([3, 1, 2, 5, 3]) == [3, 4]
assert obj.missingNumber([3, 1, 2, 5, 4, 6, 7, 5]) == [5, 8]
