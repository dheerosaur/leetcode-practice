#
# @lc app=leetcode id=118 lang=python3
# [algorithms] - Easy
#
# [118] Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/description/
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
from typing import List


class Solution:
    def new_row(self, row: List[int]) -> List[int]:
        ret = [row[0]]
        for i in range(len(row)-1):
            ret.append(row[i] + row[i+1])
        ret.append(row[-1])
        return ret

    def generate2(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for _ in range(numRows - 1):
            result.append(self.new_row(result[-1]))
        return result if numRows else []

    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal


def test():
    sol = Solution()
    cases = [
        0, 1, 4, 5, 8
    ]
    for case in cases:
        print(sol.generate(case))


if __name__ == '__main__':
    test()
