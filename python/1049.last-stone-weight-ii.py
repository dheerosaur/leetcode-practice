from typing import List


class Solution:

    def lastStoneWeight(self, A: List[int]) -> int:
        dp = {0}
        for a in A:
            dp = {a + i for i in dp} | {a - i for i in dp}
        return min(abs(x) for x in dp)


def test():
    sol = Solution()
    cases = [
        [2, 7, 4, 1, 8, 1],
        [2, 2, 2, 2],
        [1, 3],
        [316, 157, 73, 106, 771, 828, 46, 212, 926, 604, 600, 992,
         71, 51, 477, 869, 425, 405, 859, 924, 45, 187, 283, 590,
         303, 66, 508, 982, 464, 398],  # expected 0
    ]
    for case in cases:
        print(sol.lastStoneWeight(case))
        # assert sol.lastStoneWeight() == sol.lastStoneWeight_2()


if __name__ == '__main__':
    test()
