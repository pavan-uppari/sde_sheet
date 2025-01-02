class StockSpanner:
    def __init__(self):
        self.prices = []
        self.pge = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        n = len(self.prices)

        while self.pge and self.prices[self.pge[-1]] <= price:
            self.pge.pop()

        res = n
        if self.pge:
            res = n - self.pge[-1] - 1

        self.pge.append(n - 1)

        return res
