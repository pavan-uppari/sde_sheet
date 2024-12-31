class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_map = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i not in close_map:
                stack.append(i)
                continue

            if not stack:
                return False
            if stack.pop() != close_map[i]:
                return False

        return stack == []
