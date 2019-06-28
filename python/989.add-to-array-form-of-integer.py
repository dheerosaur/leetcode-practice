#
# @lc app=leetcode id=989 lang=python3
# [algorithms] - Easy
#
# [989] Add to Array-Form of Integer
# https://leetcode.com/problems/add-to-array-form-of-integer/description/
#
# For a non-negative integer X, the array-form of X is an array of its digits
# in left to right order.  For example, if X = 1231, then the array form is
# [1,2,3,1].
#
# Given the array-form A of a non-negative integer X, return the array-form of
# the integer X+K.
#
# Input: A = [1,2,0,0], K = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
#
# Input: A = [2,7,4], K = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
#
# Input: A = [2,1,5], K = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
#
# Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
# Output: [1,0,0,0,0,0,0,0,0,0,0]
# Explanation: 9999999999 + 1 = 10000000000
#
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# If A.length > 1, then A[0] != 0
from typing import List


class Solution:
    # def addToArrayForm_simple(self, A: List[int], K: int) -> List[int]:
    #     total = int(''.join(str(i) for i in A)) + K
    #     return [int(i) for i in str(total)]

    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        for i in reversed(range(len(A))):
            if K == 0 and carry == 0:
                break
            K, unit = divmod(K, 10)
            carry, A[i] = divmod(A[i] + carry + unit, 10)
        if carry or K:
            A = [int(i) for i in str(K + carry)] + A
        return A


def test():
    methods = [getattr(Solution(), m)
               for m in dir(Solution)
               if not m.startswith('_')]
    cases = [
        ([9], 999),
        ([1, 2, 0, 0], 34),
        ([2, 7, 4], 181),
        ([9, 9, 9, 9, 9], 1),
    ]
    for case in cases:
        for method in methods:
            print(method(*case))


if __name__ == '__main__':
    test()
