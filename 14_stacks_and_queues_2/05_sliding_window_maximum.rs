impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut deque: Vec<usize> = Vec::new();
        let mut res: Vec<i32> = Vec::new();

        for (ind, num) in nums.iter().enumerate() {
            if !deque.is_empty() && deque[0] as i32 <= ind as i32 - k {
                deque.remove(0);
            }

            while !deque.is_empty() && nums[*deque.last().unwrap()] <= *num {
                deque.pop();
            }

            deque.push(ind);
            if ind >= (k - 1) as usize {
                res.push(nums[deque[0]]);
            }
        }

        res
    }
}