from typing import List


class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        left = len(A) - 2
        while left >= 0 and A[left] <= A[left + 1]:
            left -= 1

        if left < 0:
            return A

        right = len(A) - 1
        while A[right] >= A[left]:
            right -= 1
        while A[right] == A[right - 1]:
            right -= 1
        A[left], A[right] = A[right], A[left]
        return A


def test():
    sol = Solution()
    cases = [
        [3, 2, 1],
        [1, 1, 5],
        [1, 9, 4, 6, 7],
        [3, 1, 1, 3],
    ]
    for case in cases:
        print(sol.prevPermOpt1(case))


if __name__ == '__main__':
    test()
