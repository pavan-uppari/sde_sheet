use std::cmp::max;
use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let n = s.len();
        if n == 0 {
            return 0;
        }
        let mut seen: HashMap<char, usize> = HashMap::new();
        let mut left = 0;
        let mut res = 0;

        for (i, ch) in s.chars().enumerate() {
            if seen.contains_key(&ch) && seen[&ch] >= left {
                res = max(res, i - left);
                left = seen[&ch] + 1;
            }
            seen.insert(ch, i);
        }

        max(res, n - left) as i32
    }
}
