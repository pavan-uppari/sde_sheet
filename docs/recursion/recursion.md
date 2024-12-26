## Sum of all Subsets

**Problem Statement**: Given an array print all the sum of the subset generated from it, in the increasing order.  
**Example**:  
Input:  N = 3, arr[] = {5,2,1}  
Output: 0,1,2,3,5,6,7,8  
Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8.  

```py
{!09_recursion/01_subset_sums.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/subset-sum-sum-of-all-subsets/) [GFG](https://www.geeksforgeeks.org/problems/subset-sums2234/1)<br>

## Print all the Unique Subsets

**Problem Statement**: Given an array of integers that may contain duplicates the task is to return all possible subsets. Return only unique subsets and they can be in any order.   
**Example**:  
Input: [1,2,2]  
Output: [[ ],[1],[1,2],[1,2,2],[2],[2,2]]  
Explanation: We can have subsets ranging from  length 0 to 3. which are listed above. Also the subset [1,2] appears twice but is printed only once as we require only unique subsets.   

```py
{!09_recursion/01_subset_sums.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/subset-ii-print-all-the-unique-subsets/) [LC](https://leetcode.com/problems/subsets-ii/)<br>

## Combination Sum - 1

**Problem Statement**: Given an array of distinct integers and a target, you have to return the list of all unique combinations where the chosen numbers sum to target. You may return the combinations in any order.  

The same number may be chosen from the given array an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

**Example**:  
Input: array = [2,3,6,7], target = 7

Output: [[2,2,3],[7]]

Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
             7 is a candidate, and 7 = 7.
             These are the only two combinations. 

```py
{!09_recursion/03_combination_sum_1.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/combination-sum-1/) [LC](https://leetcode.com/problems/combination-sum/)<br>

## Combination Sum - 2

**Problem Statement**: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

**Example**:  
Input: candidates = [10,1,2,7,6,1,5], target = 8

Output: 
[[1,1,6],[1,2,5],[1,7],[2,6]]

```py
{!09_recursion/04_combination_sum_2.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/combination-sum-ii-find-all-unique-combinations/) [LeetCode](https://leetcode.com/problems/combination-sum-ii/)<br>

## Palindrome Partitioning

**Problem Statement**: You are given a string s, partition it in such a way that every substring is a palindrome. Return all such palindromic partitions of s.

**Example**:  
Input: s = “aab”

Output: [ ["a","a","b"], ["aa","b"] ]	

```py
{!09_recursion/05_palindrom_paritioning.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/palindrome-partitioning/) [LeetCode](https://leetcode.com/problems/palindrome-partitioning/)<br>

## Find K-th Permutation Sequence

Coming Soon