## Problem Heading

**Problem Statement**: Problem statement  
**Example**:  
Input:  N = 6  start = {1,3,0,5,8,5}  end =  {2,4,5,7,9,9}  
Output: 1 2 4 5  
**Algorithm**:  
1. Find n % k where n is length of linked list, because that k is the correct value to rotate at the end.  
2. Use slow and fast pointers. Give fast pointer k steps ahead start.  

```py
{!6_linked_list_and_arrays/1_rotate_nked_list.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/rotate-a-linnnked-list/) [LeetCode](https://leetcode.com/problems/rotttate-list/)<br>