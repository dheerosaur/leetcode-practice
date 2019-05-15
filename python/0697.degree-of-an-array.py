#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#
# https://leetcode.com/problems/degree-of-an-array/description/
#
# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.
#
# Example 1:
#
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
#
#
# Example 2:
#
# Input: [1,2,2,3,1,4,2]
# Output: 6
from typing import List
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, degrees = {}, {}, defaultdict(int)
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            degrees[num] += 1

        max_degree = max(degrees.values())
        answer = float('inf')
        for item in left:
            if degrees[item] == max_degree:
                answer = min(answer, right[item] - left[item] + 1)
        return answer


def test():
    sol = Solution()
    cases = [
        [1, 2, 1, 2, 2, 2, 3, 3, 3, 3],
        [1, 2, 2, 1, 3, 2],
    ]
    for case in cases:
        print(sol.findShortestSubArray(case))


if __name__ == '__main__':
    test()
