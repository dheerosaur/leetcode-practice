#
# @lc app=leetcode id=136 lang=python3
# [algorithms] - Easy
#
# [136] Single Number
# https://leetcode.com/problems/single-number/description/
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
#
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4
from typing import List
from functools import reduce
from operator import xor


class Solution:
    def singleNumber_xor(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

    def singleNumber_set(self, nums: List[int]) -> int:
        s = set([])
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        return s.pop() if s else 0

    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)


def test():
    sol = Solution()
    cases = [
        [1, 2, 2, 3, 3],
        [4, 2, 2, 3, 3],
    ]
    for case in cases:
        print(sol.singleNumber_xor(case))


if __name__ == '__main__':
    test()
