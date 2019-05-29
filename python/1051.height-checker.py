from typing import List


class Solution:

    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 for x, y in zip(heights, sorted(heights)) if x != y)


def test():
    sol = Solution()
    cases = [
        [1, 1, 4, 2, 1, 3],
        [1, 1, 4, 2, 1, 2, 5, 3],
        [1, 2, 1, 2, 1, 1, 1, 2, 1],
    ]
    for case in cases:
        print(sol.heightChecker(case))


if __name__ == '__main__':
    test()
