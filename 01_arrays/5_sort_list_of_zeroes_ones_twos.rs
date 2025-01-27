impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let n = nums.len();
        let mut l: usize = 0;
        let mut r: usize = n - 1;
        let mut curr: usize = 0;

        while curr <= r {
            if nums[curr] == 0 {
                nums.swap(l, curr);
                l += 1;
                curr += 1;
            } else if nums[curr] == 2 {
                nums.swap(r, curr);
                if r == 0 {
                    break;
                }
                r -= 1;
            } else {
                curr += 1
            }
        }
    }
}
