use std::cmp::max;

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut res = nums[0];
        let mut curr = nums[0];

        for num in &nums[1..] {
            if curr < 0 {
                curr = 0;
            }
            curr += num;
            res = max(res, curr);
        }
        res
    }
}
