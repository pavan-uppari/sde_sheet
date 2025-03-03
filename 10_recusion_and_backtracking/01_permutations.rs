use std::collections::HashSet;

impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {

        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut seen: HashSet<usize> = HashSet::new();
        let mut curr: Vec<i32> = Vec::new();
        Solution::helper(&mut curr, &nums, &mut seen, &mut res);

        res
        
    }

    fn helper(curr: &mut Vec<i32>, nums: &Vec<i32>, seen: &mut HashSet<usize>, res: &mut Vec<Vec<i32>>){

        if seen.len() == nums.len(){
            res.push(curr.clone());
        }

        for i in 0..nums.len(){
            if !seen.contains(&i){
                seen.insert(i);
                curr.push(nums[i]);
                Solution::helper(curr, nums, seen, res);
                seen.remove(&i);
                curr.pop();
            }
        }
    }
}