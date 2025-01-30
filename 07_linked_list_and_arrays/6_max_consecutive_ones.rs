use std::cmp::max;

impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let (mut curr, mut res) = (0, 0);
        for &num in &nums {
            if num != 1 {
                res = max(res, curr);
                curr = 0;
            } else {
                curr += 1;
            }
        }
        max(res, curr)
    }
}
