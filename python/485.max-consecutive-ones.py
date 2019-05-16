#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
# Easy (54.96%)
#
# https://leetcode.com/problems/max-consecutive-ones/description/

# Given a binary array, find the maximum number of consecutive 1s in this
# array.
#
# Example 1:
#
# Input: [1,1,0,1,1,1]
# Output: 3
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len, start = 0, 0
        for i, num in enumerate(nums):
            if num == 1:
                max_len = max(max_len, i - start + 1)
            else:
                start = i + 1
        return max_len


def test():
    sol = Solution()
    cases = [
        [1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 0],
        [1],
    ]
    for case in cases:
        print(sol.findMaxConsecutiveOnes(case))


if __name__ == '__main__':
    test()
