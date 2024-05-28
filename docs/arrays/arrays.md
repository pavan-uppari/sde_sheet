## Set Matrix Zeroes

**Problem Statement**: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.<br>
**Algorithm**:<br>
1. First find the indexes of rows and columns where 0 is present<br>
2. Iterate through matrix again to make relevant items to zero<br>


```py
{!1_arrays/1_set_matrix_zeroes.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/set-matrix-zero/) [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/)<br>

## Next Permutation

Coming Soon

## Pascals Triangle

**Problem Statement**: In Pascal’s triangle, each number is the sum of the two numbers directly above it as shown in the figure below:
Given the number of rows n. Print the first n rows of Pascal’s triangle..<br>
![image](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

```py
{!1_arrays/2_pascals_triangle.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/) [LeetCode](https://leetcode.com/problems/pascals-triangle/)<br>

## Kadanes Algorithm
**Problem Statement**: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum<br>
```py
{!1_arrays/4_kadanes_algorithm.py!}
```
Links: [TUF](https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/) [LeetCode](https://leetcode.com/problems/maximum-subarray/)

## Sort list Of 0s,1s,2s
**Problem Statement**: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)<br>
```py
{!1_arrays/5_sort_list_of_zeros_ones_twos.py!}
```
Links: [TUF](https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/) [LeetCode](https://leetcode.com/problems/sort-colors/)

## Stock Buy and Sell

**Problem Statement**: You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.<br>
```py
{!1_arrays/6_stock_buy_and_sell.py!}
```
Links: [TUF](https://takeuforward.org/data-structure/stock-buy-and-sell/) [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)