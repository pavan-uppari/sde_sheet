use std::collections::HashMap;

impl Solution {
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut stack: Vec<i32> = vec![];
        let mut nge_map: HashMap<i32, i32> = HashMap::new();

        for num in nums2.iter().rev() {
            while !stack.is_empty() && stack.last().unwrap() <= num {
                stack.pop();
            }

            nge_map.insert(*num, *stack.last().unwrap_or(&-1));
            stack.push(*num);
        }

        Vec::from_iter(nums1.iter().map(|num| nge_map[num]))
    }
}
