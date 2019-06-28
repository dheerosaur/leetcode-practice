#
# @lc app=leetcode id=137 lang=python3
# [algorithms] - Medium
#
# [137] Single Number II
# https://leetcode.com/problems/single-number-ii/description/
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Input: [2,2,3,2]
# Output: 3
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
from typing import List
import collections


class Solution:
    def singleNumber_bf(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return next(k for k in counter if counter[k] != 3)


def test():
    sol = Solution()
    cases = [
        [2, 2, 3, 2],
        [0, 1, 1, 0, 1, 0, 99],
    ]
    for case in cases:
        v1 = sol.singleNumber_bf(case)
        print(v1)


if __name__ == '__main__':
    test()
