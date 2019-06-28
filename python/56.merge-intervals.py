#
# @lc app=leetcode id=56 lang=python3
# [algorithms] - Medium
#
# [56] Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
#
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for start, end in sorted(intervals):
            if result and result[-1][-1] >= start:
                result[-1][-1] = max(result[-1][-1], end)
            else:
                result.append([start, end])
        return result


def test():
    sol = Solution()
    cases = [
        [],
        [[1, 4], [1, 5]],
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
    ]
    for case in cases:
        print(sol.merge(case))


if __name__ == '__main__':
    test()
