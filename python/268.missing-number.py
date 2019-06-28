#
# @lc app=leetcode id=268 lang=python3
# [algorithms] - Easy
#
# [268] Missing Number
# https://leetcode.com/problems/missing-number/description/
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
#
# Input: [3,0,1]
# Output: 2
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
from typing import List


class Solution:
    def missingNumber_xor(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing = missing ^ i ^ num
        return missing

    def missingNumber_gauss(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

    def missingNumber_sort(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return i
        return len(nums)

    def missingNumber_hset(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums)):
            if i not in s:
                return i
        return len(nums)


def test():
    sol = Solution()
    cases = [
        [0],
        [3, 0, 1],
        [0, 1, 2],
        [x for x in range(92) if x != 30]
    ]
    for case in cases:
        v1 = sol.missingNumber_xor(case)
        v2 = sol.missingNumber_gauss(case)
        v3 = sol.missingNumber_sort(case)
        v4 = sol.missingNumber_hset(case)
        print(v1, v2, v3, v4)


if __name__ == '__main__':
    test()
