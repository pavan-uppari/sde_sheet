impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let n = matrix.len();
        let m = matrix[0].len();

        let (mut low, mut high) = (0, n * m - 1);

        while low <= high {
            let mid = (low + high) / 2;
            let (r, c) = (mid / m, mid % m);
            if matrix[r][c] == target {
                return true;
            } else if matrix[r][c] < target {
                low = mid + 1;
            } else {
                if mid == 0 {
                    break;
                }
                high = mid - 1;
            }
        }
        false
    }
}
