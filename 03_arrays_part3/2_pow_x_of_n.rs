impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        if n == 0 {
            return 1.0;
        }

        let mut x = x;
        let ox = x.clone(); //original x
        let mut dn = if n == i32::MIN { i32::MAX } else { n.abs() }; //duplicate n
        let mut res = 1.0;

        while dn > 1 {
            if dn % 2 == 1 {
                res *= x;
                dn -= 1;
            } else {
                x *= x;
                dn /= 2;
            }
        }
        res *= x;
        if n == i32::MIN {
            res *= ox;
        }
        if n < 0 {
            res = 1.0 / res;
        }

        res
    }
}
