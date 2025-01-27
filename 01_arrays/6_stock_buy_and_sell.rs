use std::cmp::{max, min};

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut mini: i32 = i32::MAX;
        let mut res: i32 = 0;
        for price in prices {
            mini = min(mini, price);
            res = max(res, price - mini);
        }
        res
    }
}
