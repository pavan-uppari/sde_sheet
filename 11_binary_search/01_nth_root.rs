fn nth_root(n: i32, m: i32) -> i32 {
    let (mut low, mut high) = (0, m);

    while low <= high {
        let mid = (low + high) / 2;
        let curr = mid.pow(n as u32);

        if curr == m {
            return mid;
        } else if curr < m {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    -1
}

fn main() {
    assert_eq!(nth_root(3, 27), 3);
    assert_eq!(nth_root(4, 69), -1);
}
