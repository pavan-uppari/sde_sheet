impl Solution {
    pub fn oranges_rotting(grid: Vec<Vec<i32>>) -> i32 {
        let mut grid = grid;
        let mut queue: Vec<(i32, i32)> = Vec::new();
        let mut rotten = 0;
        let (n, m) = (grid.len() as i32, grid[0].len() as i32);

        for i in 0..n {
            for j in 0..m {
                let i = i as usize;
                let j = j as usize;
                if grid[i][j] == 2 {
                    rotten += 1;
                    queue.push((i as i32, j as i32));
                }
            }
        }

        let mut res = -1;

        while !queue.is_empty() {
            for _ in 0..queue.len() {
                let curr = queue.remove(0);

                let x_iter: Vec<i32> = vec![1, 0, -1, 0];
                let y_iter: Vec<i32> = vec![0, 1, 0, -1];

                for i in 0..4 {
                    let new_i = curr.0 + x_iter[i];
                    let new_j = curr.1 + y_iter[i];
                    if 0 <= new_i
                        && new_i < n
                        && 0 <= new_j
                        && new_j < m
                        && grid[new_i as usize][new_j as usize] == 1
                    {
                        grid[new_i as usize][new_j as usize] = 2;
                        queue.push((new_i, new_j));
                    }
                }
            }
            res += 1;
        }

        for i in 0..n {
            for j in 0..m {
                if grid[i as usize][j as usize] == 1 {
                    return -1;
                }
            }
        }
        if rotten == 0 {
            return 0;
        }

        res
    }
}
