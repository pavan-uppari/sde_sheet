use std::collections::HashSet;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        let mut res: HashSet<(i32, i32, i32)> = HashSet::new();
        nums.sort();
        let n = nums.len();

        for i in 0..n {
            let (mut l, mut r) = (i + 1, n - 1);
            while l < r {
                let curr = nums[i] + nums[l] + nums[r];
                if curr == 0 {
                    res.insert((nums[i], nums[l], nums[r]));
                    l += 1;
                    r -= 1;
                } else if curr > 0 {
                    r -= 1;
                } else {
                    l += 1;
                }
            }
        }

        let mut return_value: Vec<Vec<i32>> = vec![];
        for item in res {
            return_value.push(vec![item.0, item.1, item.2]);
        }
        return_value
    }
}
