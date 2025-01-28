fn find_duplicate(nums: Vec<i32>) -> (i32, i32) {
    let n: i32 = nums.len() as i32;
    let sn: i32 = n * (n + 1) / 2;
    let s2n: i32 = n * (n + 1) * (2 * n + 1) / 6;

    let mut c_sn = 0;
    let mut c_s2n = 0;
    for num in nums {
        c_sn += num;
        c_s2n += num * num;
    }

    let eq1 = (c_s2n - s2n) / (c_sn - sn);
    let eq2 = c_sn - sn;

    ((eq1 + eq2) / 2, (eq1 - eq2) / 2)
}

fn main() {
    assert_eq!((3, 4), find_duplicate(vec![3, 1, 2, 5, 3]));
    assert_eq!((5, 8), find_duplicate(vec![3, 1, 2, 5, 4, 6, 7, 5]));
}
