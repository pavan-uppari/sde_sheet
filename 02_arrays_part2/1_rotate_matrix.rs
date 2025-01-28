impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();
        let m = matrix[0].len();

        for i in 0..n {
            for j in i + 1..m {
                let temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        for i in 0..n {
            matrix[i].reverse();
        }
    }
}
