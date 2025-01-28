use std::collections::HashSet;

impl Solution {
    pub fn four_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();
        let n = nums.len();
        let mut res: HashSet<(i32, i32, i32, i32)> = HashSet::new();

        for i in 0..n {
            for j in i + 1..n {
                let (mut l, mut r) = (j + 1, n - 1);
                let req = target as i64 - nums[i] as i64 - nums[j] as i64;
                while l < r {
                    if (nums[l] + nums[r]) as i64 == req {
                        res.insert((nums[i], nums[j], nums[l], nums[r]));
                        l += 1;
                        r -= 1;
                    } else if ((nums[l] + nums[r]) as i64) < req {
                        l += 1;
                    } else {
                        r -= 1;
                    }
                }
            }
        }

        let mut return_value: Vec<Vec<i32>> = vec![];
        for (a, b, c, d) in res {
            return_value.push(vec![a, b, c, d]);
        }
        return_value
    }
}
