use std::collections::HashSet;

impl Solution {
    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut candidates = candidates;
        candidates.sort();

        let mut res: HashSet<Vec<i32>> = HashSet::new();
        let mut curr: Vec<i32> = Vec::new();
        Solution::helper(0, 0, &mut curr, &candidates, target, &mut res);

        let mut res_vec: Vec<Vec<i32>> = Vec::new();
        for i in res {
            res_vec.push(i);
        }

        res_vec
    }

    fn helper(
        ind: usize,
        curr_sum: i32,
        curr: &mut Vec<i32>,
        candidates: &Vec<i32>,
        target: i32,
        res: &mut HashSet<Vec<i32>>,
    ) {
        if curr_sum == target {
            res.insert(curr.clone());
            return;
        }

        if curr_sum > target || ind == candidates.len() {
            return;
        }

        curr.push(candidates[ind]);
        Solution::helper(
            ind + 1,
            curr_sum + candidates[ind],
            curr,
            candidates,
            target,
            res,
        );

        curr.pop();
        for i in ind + 1..candidates.len() {
            if candidates[i] != candidates[ind] {
                Solution::helper(i, curr_sum, curr, candidates, target, res);
                break;
            }
        }
    }
}
