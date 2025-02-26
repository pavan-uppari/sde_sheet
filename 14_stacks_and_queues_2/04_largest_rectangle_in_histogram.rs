use std::cmp::max;

impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let nse_vec: Vec<i32> = Solution::nse(&heights);
        let pse_vec: Vec<i32> = Solution::pse(&heights);

        let mut res: i32 = 0;

        for i in 0..heights.len() {
            res = max(res, heights[i] * (nse_vec[i] - pse_vec[i] - 1))
        }
        res
    }

    pub fn nse(heights: &Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = vec![];
        let mut stack: Vec<i32> = vec![];
        let n: i32 = heights.len() as i32;

        for ind in (0..heights.len()).rev() {
            while !stack.is_empty() && heights[*stack.last().unwrap() as usize] >= heights[ind] {
                stack.pop();
            }
            res.push(*stack.last().unwrap_or(&n));
            stack.push(ind as i32);
        }
        res.reverse();
        res
    }

    pub fn pse(heights: &Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = vec![];
        let mut stack: Vec<i32> = vec![];

        for ind in 0..heights.len() {
            while !stack.is_empty() && heights[*stack.last().unwrap() as usize] >= heights[ind] {
                stack.pop();
            }
            res.push(*stack.last().unwrap_or(&-1));
            stack.push(ind as i32);
        }
        res
    }
}
