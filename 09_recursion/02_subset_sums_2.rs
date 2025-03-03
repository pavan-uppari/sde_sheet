use std::collections::HashSet;

impl Solution {
    pub fn subsets_with_dup(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();
        let mut res: HashSet<Vec<i32>> = HashSet::new();
        let mut curr: Vec<i32> = Vec::new();
        Solution::helper(0, &mut curr, &nums, &mut res);

        let mut vec_res: Vec<Vec<i32>> = Vec::new();

        for i in res {
            vec_res.push(i);
        }

        vec_res
    }

    fn helper(ind: usize, curr: &mut Vec<i32>, nums: &Vec<i32>, res: &mut HashSet<Vec<i32>>) {
        if ind == nums.len() {
            res.insert(curr.clone());
            return;
        }

        curr.push(nums[ind]);
        Solution::helper(ind + 1, curr, nums, res);

        curr.pop();
        Solution::helper(ind + 1, curr, nums, res);
    }
}
