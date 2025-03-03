fn subset_sums(nums: &Vec<i32>) -> Vec<i32> {
    let mut res: Vec<i32> = Vec::new();
    helper(0, 0, nums, &mut res);

    res.sort();
    res
}

fn helper(ind: usize, curr_sum: i32, nums: &Vec<i32>, res: &mut Vec<i32>) {
    if ind == nums.len() {
        res.push(curr_sum);
        return;
    }

    helper(ind + 1, curr_sum + nums[ind], nums, res);
    helper(ind + 1, curr_sum, nums, res);
}

fn main() {
    assert_eq!(subset_sums(&vec![2, 3]), vec![0, 2, 3, 5]);
    assert_eq!(subset_sums(&vec![1, 2, 1]), vec![0, 1, 1, 2, 2, 3, 3, 4]);
    assert_eq!(subset_sums(&vec![5, 6, 7]), vec![0, 5, 6, 7, 11, 12, 13, 18]);
}
