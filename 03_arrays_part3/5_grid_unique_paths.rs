use std::collections::HashMap;

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let mut dp: HashMap<(i32, i32), i32> = HashMap::new();
        return Solution::helper(0, 0, m, n, &mut dp);
    }

    fn helper(r: i32, c: i32, m: i32, n: i32, dp: &mut HashMap<(i32, i32), i32>) -> i32 {
        if dp.contains_key(&(r, c)) {
            return dp[&(r, c)];
        }

        if r == m || c == n {
            return 0;
        }
        if r == m - 1 && c == n - 1 {
            return 1;
        }

        let left = Solution::helper(r, c + 1, m, n, dp);
        let right = Solution::helper(r + 1, c, m, n, dp);

        dp.insert((r, c), left + right);
        return dp[&(r, c)];
    }
}
