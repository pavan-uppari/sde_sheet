fn nse(nums: Vec<i32>) -> Vec<i32> {
    let mut stack: Vec<i32> = vec![];
    let mut res: Vec<i32> = vec![];

    for num in nums.iter().rev() {
        while !stack.is_empty() && stack.last().unwrap() >= num {
            stack.pop();
        }
        res.push(*stack.last().unwrap_or(&-1));
        stack.push(*num);
    }

    res.reverse();
    res
}

fn main() {
    assert_eq!(nse(vec![4, 5, 2, 10, 8]), vec![2, 2, -1, 8, -1]);
    assert_eq!(nse(vec![3, 2, 1]), vec![2, 1, -1]);
    assert_eq!(nse(vec![1, 2, 3]), vec![-1, -1, -1]);
}
