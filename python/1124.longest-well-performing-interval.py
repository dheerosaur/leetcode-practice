from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res, score = 0, 0
        sums = []
        seen = {}
        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1
            sums.append(score)
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res


def test():
    sol = Solution()
    cases = [
        # cases
        [0, 0, 0, 9, 9, 6, 0, 6, 6, 9, 9, 9]
    ]
    for case in cases:
        print(sol.longestWPI(case))


if __name__ == "__main__":
    test()
