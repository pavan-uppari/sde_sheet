impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {

        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut curr: Vec<i32> = Vec::new();
        Solution::helper(0, 0, &mut curr, &candidates, target, &mut res);

        res
        
    }

    fn helper(ind: usize, curr_sum: i32, curr: &mut Vec<i32>, candidates: &Vec<i32>, target: i32, res: &mut Vec<Vec<i32>>){

        if curr_sum == target{
            res.push(curr.clone());
            return;
        }

        if curr_sum > target || ind == candidates.len(){
            return;
        }

        curr.push(candidates[ind]);
        Solution::helper(ind, curr_sum + candidates[ind], curr, candidates, target, res);

        curr.pop();
        Solution::helper(ind+1, curr_sum, curr, candidates, target, res);



    }
}