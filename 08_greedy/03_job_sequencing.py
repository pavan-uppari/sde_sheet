class Solution:
    def JobSequencing(self, ids, deadline, profit):
        ids, deadline, profit = zip(
            *sorted(zip(ids, deadline, profit), key=lambda x: x[2], reverse=True)
        )
        cnt = total_profit = 0
        jobs = [None] * (max(deadline) + 1)

        for _, a, b in zip(ids, deadline, profit):
            for day in range(a, 0, -1):
                if not jobs[day]:
                    jobs[day] = b
                    cnt += 1
                    total_profit += b
                    break

        return cnt, total_profit
