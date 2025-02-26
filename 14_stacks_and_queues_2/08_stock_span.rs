struct StockSpanner {
    stocks: Vec<i32>,
    pge: Vec<i32>,
}

impl StockSpanner {
    fn new() -> Self {
        StockSpanner {
            stocks: Vec::new(),
            pge: Vec::new(),
        }
    }

    fn next(&mut self, price: i32) -> i32 {
        self.stocks.push(price);
        let n = self.stocks.len() as i32;

        while !self.pge.is_empty() && self.stocks[*self.pge.last().unwrap() as usize] <= price {
            self.pge.pop();
        }
        let mut res = n;

        if !self.pge.is_empty() {
            res = n - *self.pge.last().unwrap() - 1;
        }
        self.pge.push(n - 1);

        res
    }
}
