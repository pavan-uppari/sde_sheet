impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut i: usize = 0;
        let mut j: usize = 0;
        let um: usize = m as usize;
        let un: usize = n as usize;

        while i < um + un && j < un {
            if nums2[j] < nums1[i] {
                nums1.pop();
                nums1.insert(i, nums2[j]);
                j += 1;
            }
            i += 1;
        }

        for i in um + j..um + un {
            nums1[i] = nums2[j];
            j += 1;
        }
    }
}
