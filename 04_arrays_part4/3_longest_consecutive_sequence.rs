use std::cmp::max;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort();
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut prev = nums[0];
        let mut count = 1;
        let mut res = 1;

        for &num in &nums[1..] {
            if num == prev {
                continue;
            } else if num == prev + 1 {
                count += 1;
            } else {
                res = max(res, count);
                count = 1;
            }
            prev = num;
        }

        max(res, count)
    }
}
