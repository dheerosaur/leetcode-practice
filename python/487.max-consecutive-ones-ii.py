# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II medium
#
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
#
# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0.
#
#
# Example 1:
#
# Input: [1,0,1,1,0]
# Output: 4
#
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other
# words, you can't store all numbers coming from the stream as it's too large
# to hold in memory. Could you solve it efficiently?
from typing import List


class Solution:
    def findMaxConsecutiveOnes_2(self, nums: List[int]) -> int:
        cur, max_len, last_zero_at = 0, 0, -1
        for i, num in enumerate(nums):
            if num == 1:
                cur += 1
            else:
                cur = i - last_zero_at
                last_zero_at = i
            max_len = max(cur, max_len)
        return max_len

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1, count2, largest = 0, 0, 0
        for num in nums:
            if num == 1:
                count1, count2 = count1 + 1, count2 + 1
            else:
                count2 = count1 + 1
                count1 = 0
            largest = max(largest, count2)
        return largest


def test():
    sol = Solution()
    cases = [
        [1, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 0],
        [1],
    ]
    for case in cases:
        print(sol.findMaxConsecutiveOnes(case))


if __name__ == '__main__':
    test()
