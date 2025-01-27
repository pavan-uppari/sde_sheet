impl Solution {
    pub fn generate(n: i32) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = vec![vec![1]];

        if n == 1 {
            return res;
        }
        for i in 2..=n {
            let last = res.last().unwrap();
            res.push(Solution::next_row(last));
        }
        res
    }

    pub fn next_row(last: &Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = vec![1];
        for i in 1..last.len() {
            res.push(last[i] + last[i - 1]);
        }
        res.push(1);
        res
    }
}
