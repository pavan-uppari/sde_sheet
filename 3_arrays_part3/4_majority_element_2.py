class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        e1 = e2 = None
        c1 = c2 = 0
        for num in nums:
            if c1 == 0 and e2 != num:
                e1 = num
                c1 = 1
            elif c2 == 0 and e1 != num:
                e2 = num
                c2 = 1
            elif num == e1:
                c1 += 1
            elif num == e2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        c1 = c2 = 0
        for num in nums:
            if num == e1:
                c1 += 1
            elif num == e2:
                c2 += 1
        n = len(nums)
        res = []
        if e1 is not None and c1 > n // 3:
            res.append(e1)
        if e2 is not None and c2 > n // 3:
            res.append(e2)
        return res
