# O(N+M) extra space for creating new array


class Solution:
    def minimumPlatform(self, arr, dep):
        times = [(a, 0) for a in arr]
        times.extend([(a, 1) for a in dep])
        times.sort()

        cnt = 0
        res = 0
        for a, b in times:
            if b:
                cnt -= 1
            else:
                cnt += 1
            res = max(res, cnt)
        return res


# No extra space used - 2 pointers approach
class Solution:
    def minimumPlatform(self, arr, dep):
        arr.sort()
        dep.sort()

        n, m = len(arr), len(dep)
        i = j = cnt = res = 0

        while i < n and j < m:
            if arr[i] <= dep[j]:
                cnt += 1
                i += 1
            else:
                cnt -= 1
                j += 1
            res = max(res, cnt)

        return res
