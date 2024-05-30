class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        """
        1. Sort the list
        2. Create res list
        3. Iterate through list and compare the item with the last item of res to check if merging is possible
        4. If possible, update the last item of res, else add current item to res
        """
        nums.sort()
        res = [nums[0]]
        for i in range(1,len(nums)):
            if res[-1][-1] >= nums[i][0]:
                res[-1] = [res[-1][0], max(res[-1][1], nums[i][1])]
            else:
                res.append(nums[i])
        return res
        