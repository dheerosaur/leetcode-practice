#
# @lc app=leetcode id=42 lang=python3
# [algorithms] - Hard
#
# [42] Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/description/
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#
# Example:
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
from typing import List


class Solution:
    def find_peak(self, items):
        peak, peak_at = 0, 0
        for i, h in enumerate(items):
            if peak < h:
                peak = h
                peak_at = i
        return peak_at

    def trap(self, height: List[int]) -> int:
        peak_at = self.find_peak(height)
        i, mx = 0, 0
        result = 0
        while i < peak_at:
            while i < peak_at and height[i] <= mx:
                result += mx - height[i]
                i += 1
            mx = height[i]

        i, mx = len(height) - 1, 0
        while i > peak_at:
            while i > peak_at and height[i] <= mx:
                result += mx - height[i]
                i -= 1
            mx = height[i]

        return result


def test():
    sol = Solution()
    cases = [
        [0, 0, 1, 0, 0, 1],
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    ]
    for case in cases:
        print(sol.trap(case))


if __name__ == '__main__':
    test()
