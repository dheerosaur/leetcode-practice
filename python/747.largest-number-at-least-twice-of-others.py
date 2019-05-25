#
# @lc app=leetcode id=747 lang=python3
# [algorithms] - Easy
#
# [747] Largest Number At Least Twice of Others
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
#
# In a given integer array nums, there is always exactly one largest element.
#
# Find whether the largest element in the array is at least twice as much as
# every other number in the array.
#
# If it is, return the index of the largest element, otherwise return -1.
#
# Example 1:
#
# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the
# array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so 1
#
# Example 2:
#
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return
# -1.
from typing import List


class Solution:
    def dominantIndex(self, A: List[int]) -> int:
        largest = max(range(len(A)), key=lambda i: A[i])
        for i, num in enumerate(A):
            if i != largest and A[largest] < (num * 2):
                return -1
        return largest

    def dominantIndex_all(self, A: List[int]) -> int:
        ans, largest = -1, -1
        for i, num in enumerate(A):
            if num >= (2 * largest):
                ans = i
            elif largest < (2 * num):
                ans = -1
            if num > largest:
                largest = num
        return ans


def test():
    sol = Solution()
    cases = [
        [3, 6, 1, 0],
        [1, 2, 3, 4],
        [3, 6, 1, 6],
        [1],
        [1, 0],
    ]
    for case in cases:
        print(sol.dominantIndex(case))


if __name__ == '__main__':
    test()
