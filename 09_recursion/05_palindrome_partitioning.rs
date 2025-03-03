impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
        let mut res: Vec<Vec<String>> = Vec::new();
        let mut curr: Vec<String> = Vec::new();
        Solution::helper(0, &mut curr, &s, &mut res);
        res
    }

    fn helper(ind: usize, curr: &mut Vec<String>, s: &String, res: &mut Vec<Vec<String>>) {
        if ind == s.len() {
            res.push(curr.clone());
            return;
        }

        for i in ind + 1..=s.len() {
            if s[ind..i] == s[ind..i].chars().rev().collect::<String>() {
                curr.push(s[ind..i].to_string());
                Solution::helper(i, curr, s, res);
                curr.pop();
            }
        }
    }
}
