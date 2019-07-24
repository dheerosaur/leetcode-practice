from typing import List


class Solution:
    def largest_range2(self, nums: List[int]) -> List[int]:
        n, A = len(nums), sorted(nums)
        i, j = 0, 0

        k = 0
        while k < n:
            m = k + 1
            while m < n and A[m] == A[m - 1] + 1:
                m += 1
            if m - k > j - i:
                i, j = k, m
            k = m
        return A[i], A[j - 1]

    def largest_range(self, nums: List[int]) -> List[int]:
        nset = set(nums)
        i = 0
        mn = mx = nums[0]

        while nset:
            if nums[i] in nset:
                nset.remove(nums[i])
            left = nums[i] - 1
            while left in nset:
                nset.remove(left)
                left -= 1

            right = nums[i] + 1
            while right in nset:
                nset.remove(right)
                right += 1

            if right - left - 2 > mx - mn:
                mx, mn = right - 1, left + 1
            i += 1
        return (mn, mx)


def test():
    sol = Solution()
    cases = [
        # cases
        [1],
        [1, 2],
        [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6],
        [1, 2, 3, 5, 6, 7, 8, 10, 11],
    ]
    for case in cases:
        print(sol.largest_range(case))


if __name__ == "__main__":
    test()
