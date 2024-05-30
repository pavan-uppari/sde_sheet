def solution(nums: list[int]) -> int:

    d: int[int] = {0:-1}
    sum = 0
    res = 0
    for i,num in enumerate(nums):
        sum+=num
        if sum in d:
            res = max(res, i-d[sum])
        else:
            d[sum] = i
    return res

assert solution([9, -3, 3, -1, 6, -5]) == 5
assert solution([6, -2, 2, -8, 1, 7, 4, -10]) == 8
assert solution([1, 0, -5]) == 1
assert solution([1, 3, -5, 6, -2]) == 0