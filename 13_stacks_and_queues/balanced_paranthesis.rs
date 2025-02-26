use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let close_map: HashMap<char, char> = HashMap::from([(']', '['), (')', '('), ('}', '{')]);
        let mut stack: Vec<char> = vec![];

        for c in s.chars() {
            if !close_map.contains_key(&c) {
                stack.push(c);
                continue;
            }

            if stack.len() == 0 || stack.pop().unwrap() != *close_map.get(&c).unwrap() {
                return false;
            }
        }

        stack.len() == 0
    }
}
