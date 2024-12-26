class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if s == "":
            return 0
        left = 0
        seen = {}
        res = 0
        for i in range(n):
            if s[i] in seen and seen[s[i]] >= left:
                res = max(res, i - left)
                left = seen[s[i]] + 1
            seen[s[i]] = i

        return max(res, i - left + 1)
