"""
Given an integer array A, you partition the array into (contiguous) subarrays
of length at most K.  After partitioning, each subarray has their values
changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.
"""
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        max_sum_until = [0] * len(A)
        curr_max = float('-inf')
        for i, val in enumerate(A[:K]):
            curr_max = max(curr_max, val)
            max_sum_until[i] = curr_max * (i + 1)
        print(max_sum_until)

        for i in range(K, len(A)):
            cur_max = float('-inf')
            max_sum = float('-inf')
            for j in range(1, K + 1):
                cur_max = max(cur_max, A[i - j + 1])
                max_sum = max(max_sum, max_sum_until[i - j] + cur_max * j)
            max_sum_until[i] = max_sum
        return max_sum_until[-1]


def test():
    sol = Solution()
    cases = [([1, 15, 7, 9, 2, 5, 10], 3)]
    for case in cases:
        print(sol.maxSumAfterPartitioning(*case))


if __name__ == '__main__':
    test()
