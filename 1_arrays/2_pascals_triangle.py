"""
https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/
https://leetcode.com/problems/pascals-triangle/

#medium

Problem Statement: 
In Pascal’s triangle, each number is the sum of the two numbers directly above it as shown in the figure below:
Given the number of rows n. Print the first n rows of Pascal’s triangle.
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
        for _ in range(2, numRows+1):
            result.append(self.next_pascal_row(result[-1]))
        return result


    def next_pascal_row(self, row: list[int]):
        result = [1]
        for i in range(1, len(row)):
            result.append(row[i] + row[i-1])
        result.append(1)
        return result
        
        