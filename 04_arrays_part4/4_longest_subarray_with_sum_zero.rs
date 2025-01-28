use std::cmp::max;
use std::collections::HashMap;

fn longest_subarray_with_zero_sum(nums: &Vec<i32>) -> i32 {
    let mut d: HashMap<i32, i32> = HashMap::new();
    d.insert(0, -1);
    let mut sum = 0;
    let mut res = 0;

    for i in 0..nums.len() {
        sum += nums[i];
        if d.contains_key(&sum) {
            res = max(res, i as i32 - d[&sum])
        } else {
            d.insert(sum, i as i32);
        }
    }
    res
}

fn main() {
    assert_eq!(
        longest_subarray_with_zero_sum(&vec![9, -3, 3, -1, 6, -5]),
        5
    );
    assert_eq!(
        longest_subarray_with_zero_sum(&vec![6, -2, 2, -8, 1, 7, 4, -10]),
        8
    );
    assert_eq!(longest_subarray_with_zero_sum(&vec![1, 0, -5]), 1);
    assert_eq!(longest_subarray_with_zero_sum(&vec![1, 3, -5, 6, -2]), 0);
}
