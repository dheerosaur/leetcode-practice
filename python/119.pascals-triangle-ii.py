#
# @lc app=leetcode id=119 lang=python3
# [algorithms] - Easy
#
# [119] Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
from typing import List


class Solution:
    def getRow2(self, rowIndex: int) -> List[int]:
        A = [1]
        for i in range(rowIndex):
            tmp = [1]
            for j in range(1, i):
                tmp.append(A[j - 1] + A[j])
            tmp.append(1)
            A = tmp
        return A

    def getRow(self, rowIndex: int) -> List[int]:
        A = [0] * (rowIndex + 1)
        A[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                A[j] += A[j - 1]
        return A


def test():
    sol = Solution()
    cases = [
        4, 5, 6, 10
    ]
    for case in cases:
        print(sol.getRow(case))


if __name__ == '__main__':
    test()
