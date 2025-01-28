use std::collections::HashSet;

impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let mut set: HashSet<i32> = HashSet::new();

        for num in nums {
            if set.contains(&num) {
                return num;
            }
            set.insert(num);
        }
        return 1;
    }
}
