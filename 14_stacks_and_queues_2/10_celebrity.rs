use std::collections::HashMap;

fn celebrity(matrix: &[[i32; 4]; 4]) -> i32 {
    let mut i_know: HashMap<usize, usize> = HashMap::new();
    let mut know_me: HashMap<usize, usize> = HashMap::new();
    let (m, n) = (matrix.len(), matrix[0].len());

    for i in 0..m {
        for j in 0..n {
            if matrix[i][j] == 1 {
                i_know.entry(i).and_modify(|e| *e += 1).or_insert(1);
                know_me.entry(j).and_modify(|e| *e += 1).or_insert(1);
            }
        }
    }

    for i in 0..n {
        if !i_know.contains_key(&i) && know_me[&i] == n - 1 {
            return i as i32;
        }
    }

    -1
}

fn main() {
    let matrix = [[0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]];
    assert_eq!(celebrity(&matrix), 1);
}
