impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> Vec<i32> {
        let (mut e1, mut e2, mut c1, mut c2) = (0, 1, 0, 0);

        for &num in &nums {
            if num == e1 {
                c1 += 1
            } else if num == e2 {
                c2 += 1
            } else if c1 == 0 {
                e1 = num;
                c1 = 1;
            } else if c2 == 0 {
                e2 = num;
                c2 = 1;
            } else {
                c1 -= 1;
                c2 -= 1;
            }
        }

        let n = nums.len();
        let (mut c1, mut c2) = (0, 0);
        for &num in &nums {
            if num == e1 {
                c1 += 1;
            }
            if num == e2 {
                c2 += 1;
            }
        }
        let mut res: Vec<i32> = vec![];
        if c1 > n / 3 {
            res.push(e1)
        }
        if c2 > n / 3 {
            res.push(e2)
        }

        res
    }
}
