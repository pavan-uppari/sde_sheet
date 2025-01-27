use std::collections::HashSet;

impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mut r: HashSet<usize> = HashSet::new();
        let mut c: HashSet<usize> = HashSet::new();

        let n = matrix.len();
        let m = matrix[0].len();

        for i in 0..n {
            for j in 0..m {
                if matrix[i][j] == 0 {
                    r.insert(i);
                    c.insert(j);
                }
            }
        }

        for i in 0..n {
            for j in 0..m {
                if r.contains(&i) || c.contains(&j) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}