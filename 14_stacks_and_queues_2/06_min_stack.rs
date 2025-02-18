use std::cmp::min;

struct MinStack {
    stack: Vec<i32>,
    min_stack: Vec<i32>,
}

impl MinStack {
    fn new() -> Self {
        MinStack {
            stack: Vec::new(),
            min_stack: Vec::new(),
        }
    }

    fn push(&mut self, val: i32) {
        if self.stack.is_empty() {
            self.min_stack.push(val);
        } else {
            let top = self.min_stack.last().unwrap();
            self.min_stack.push(min(*top, val));
        }
        self.stack.push(val);
    }

    fn pop(&mut self) {
        self.stack.pop();
        self.min_stack.pop();
    }

    fn top(&self) -> i32 {
        *self.stack.last().unwrap()
    }

    fn get_min(&self) -> i32 {
        *self.min_stack.last().unwrap()
    }
}
