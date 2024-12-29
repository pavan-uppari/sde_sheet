## Rotate a Linked List

**Problem Statement**: Rotate the list to the right by k places.<br>
**Algorithm**:<br>
1. Find n % k where n is length of linked list, because that k is the correct value to rotate at the end<br>
2. Use slow and fast pointers. Give fast pointer k steps ahead start.<br>
3. Now move slow and fast pointer simultaneoulsy till fast pointer reaches end to find the kth point<br>
4. Change the corresponding node next values

```py
{!07_linked_list_and_arrays/1_rotate_linked_list.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/rotate-a-linked-list/) [LeetCode](https://leetcode.com/problems/rotate-list/)<br>

---

## 3Sum

**Problem Statement**: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.<br>
**Algorithm1 - Using HashMap**:<br>
1. Iterate through array. For every iteration, perform 2 sum using hashmap<br>
2. Sort the array to avoid duplicates<br>

**Algorithm2 - Using BinarySearch**:<br>
1. Sort the array<br>
2. Iterate through array. For every iteration, perform binary search approach<br>
3. Use left and right pointers. If sum is greater than zero, increase left else decrease right.<br>
4. If sum is zero, add items to res<br>

```py
{!07_linked_list_and_arrays/3_3sum.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/) [LeetCode](https://leetcode.com/problems/3sum/)<br>

---

## Trapping Rainwater

**Problem Statement**: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Example**:  

![rainwater](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

**Algorithm**:  
At a particular index, amount of water that can be trapped is height - min(prefix_max_height, suffix_max_height)

```py
{!07_linked_list_and_arrays/4_trapping_rainwater.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/trapping-rainwater/) [LC](https://leetcode.com/problems/trapping-rain-water/description/)<br>

---

## Remove duplicates from sorted array

**Problem Statement**: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.<br>
**Algorithm**:<br>
1. Use a curr pointer. Till curr pointer elements are correct<br>
2. Iterate through array and find whether current elements is same as previous. If not, put that value in curr pointer and increase curr pointer value<br>
3. The required length is till curr<br>

```py
{!07_linked_list_and_arrays/5_remove_duplicates_from_sorted_array.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/) [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)<br>

---

## Max Consecutive Ones

**Problem Statement**: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.<br>
**Algorithm**:<br>
1. Iterate through array, it element is 1, increment counter<br>
2. Else, res is maximum of res and curr<br>

```py
{!07_linked_list_and_arrays/6_max_consecutive_ones.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array/) [LeetCode](https://leetcode.com/problems/max-consecutive-ones/)<br>