def nextSmallerElement(A, n):
    stack = []
    res = []
    for a in A[::-1]:
        while stack and stack[-1] >= a:
            stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(a)

    return res[::-1]
