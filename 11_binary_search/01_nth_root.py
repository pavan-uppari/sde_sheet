def NthRoot(n: int, m: int) -> int:
    low, high = 0, m

    while low <= high:
        mid = (low + high) // 2

        curr = mid**n

        if curr == m:
            return mid
        elif curr < m:
            low = mid + 1
        else:
            high = mid - 1

    return -1
