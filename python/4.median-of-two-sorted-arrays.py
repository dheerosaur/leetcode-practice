#
# @lc app=leetcode id=4 lang=python3
# [algorithms] - Hard
#
# [4] Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
from typing import List


class Solution:
    # TODO: Implement the binary search approach
    def findMedianSortedArrays(self, A: List[int], B: List[int]):
        len1, len2 = len(A), len(B)
        m1, m2 = (len1 + len2 - 1) // 2, (len1 + len2) // 2
        i, j, k, current = 0, 0, -1, None
        nums = []
        while k < m2:
            if j >= len2 or (i < len1 and A[i] <= B[j]):
                i, current = i + 1, A[i]
            else:
                j, current = j + 1, B[j]
            k += 1
            if k == m1:
                nums.append(current)
            if k == m2:
                nums.append(current)
        return sum(nums) / 2


def test():
    sol = Solution()
    cases = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
    ]
    for case in cases:
        print(sol.findMedianSortedArrays(*case))


if __name__ == '__main__':
    test()
