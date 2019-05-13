"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m
+ n) to hold additional elements from nums2.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i < 0 or nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j = j - 1
            elif i >= 0:
                nums1[k] = nums1[i]
                i = i - 1
            k = k - 1
        return nums1


def test():
    sol = Solution()
    cases = [
        [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
        [[7, 8, 8, 0, 0, 0], 3, [2, 5, 6], 3],
        [[1, 2, 4, 5, 6, 0], 5, [3], 1],
    ]
    for case in cases:
        print(sol.merge(*case))


if __name__ == '__main__':
    test()
