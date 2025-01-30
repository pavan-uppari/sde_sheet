use std::cmp::{max, min};

impl Solution {
    pub fn trap(heights: Vec<i32>) -> i32 {
        let (mut pmax, mut smax) = (0, 0);
        let mut pmax_vec: Vec<i32> = vec![];
        let mut smax_vec: Vec<i32> = vec![];
        let n = heights.len();

        for (i, &height) in heights.iter().enumerate() {
            pmax = max(pmax, height);
            pmax_vec.push(pmax);

            smax = max(smax, heights[n - i - 1]);
            smax_vec.push(smax);
        }

        let mut res = 0;
        smax_vec.reverse();
        for i in 0..n {
            res += min(pmax_vec[i], smax_vec[i]) - heights[i];
        }

        res
    }
}
