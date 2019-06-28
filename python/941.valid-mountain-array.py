#
# @lc app=leetcode id=941 lang=python3
# [algorithms] - Easy
#
# [941] Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/description/
#
# Given an array A of integers, return true if and only if it is a valid
# mountain array.
#
# Recall that A is a mountain array if and only if:
#
#
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
#
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
#
# Input: [2,1]
# Output: false
#
# Input: [3,5,5]
# Output: false
#
# Input: [0,3,2,1]
# Output: true
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000 
from typing import List


class Solution:
    def validMountainArray_one(self, A: List[int]) -> bool:
        i, last = 0, len(A) - 1
        while i < last and A[i] < A[i + 1]:
            i += 1
        if i in (0, last):
            return False
        while i < last and A[i] > A[i + 1]:
            i += 1
        return i == last

    def validMountainArray(self, A: List[int]) -> bool:
        i, j, last = 0, len(A) - 1, len(A) - 1
        while i < last and A[i] < A[i + 1]:
            i += 1
        while j > 0 and A[j - 1] > A[j]:
            j -= 1
        return i > 0 and i == j and j < last


def test():
    sol = Solution()
    cases = [
        [2, 1],
        [3, 5, 5],
        [0, 3, 2, 1],
        [0, 1, 2, 3, 2, 1],
        [0, 1, 2, 3],
    ]
    for case in cases:
        print(sol.validMountainArray(case))


if __name__ == '__main__':
    test()
