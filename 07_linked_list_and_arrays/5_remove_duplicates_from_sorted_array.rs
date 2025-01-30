impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let n = nums.len();
        let mut curr = 1;

        for i in 1..n {
            if nums[i] == nums[i - 1] {
                continue;
            }
            nums[curr] = nums[i];
            curr += 1;
        }
        curr as i32
    }
}
