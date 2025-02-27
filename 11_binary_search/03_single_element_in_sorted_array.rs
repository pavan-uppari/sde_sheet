impl Solution {
    pub fn single_non_duplicate(nums: Vec<i32>) -> i32 {
        let n = nums.len();

        if n == 1 || nums[0] != nums[1] {
            return nums[0];
        }
        if nums[n - 1] != nums[n - 2] {
            return nums[n - 1];
        }

        let (mut low, mut high) = (1, n - 2);

        while low <= high {
            let mid = (low + high) / 2;

            if nums[mid] != nums[mid - 1] && nums[mid] != nums[mid + 1] {
                return nums[mid];
            } else if nums[mid] != nums[mid - 1] {
                if mid % 2 == 1 {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else {
                if mid % 2 == 1 {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }

        1
    }
}
