use std::cmp::max;

impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut intervals = intervals;

        intervals.sort();
        let mut res: Vec<Vec<i32>> = vec![intervals[0].clone()];

        for interval in &intervals[1..] {
            let last = res.last().unwrap().to_vec();
            if interval[0] <= last[1] {
                res.pop();
                res.push(vec![last[0], max(last[1], interval[1])]);
            } else {
                res.push(interval.to_vec());
            }
        }
        res
    }
}
