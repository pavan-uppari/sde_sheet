use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, i32> = HashMap::new();

        for i in 0..nums.len() {
            let ii: i32 = i as i32;
            let req = target - nums[i];
            if seen.contains_key(&req) {
                return vec![seen[&req], ii];
            }
            seen.insert(nums[i], ii);
        }
        vec![]
    }
}
