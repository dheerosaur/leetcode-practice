"""
Grumpy Bookstore Owner
"""
from typing import List


class Solution:

    def maxSatisfied2(self, customers: List[int],
                      grumpy: List[int], X: int) -> int:
        def flipped(i):
            start, end = i - X, i
            return sum(x for x, y in
                       zip(customers[start: end], grumpy[start: end])
                       if y)
        default = sum(c for i, c in enumerate(customers) if grumpy[i] == 0)
        return max((default + flipped(i)) for i in range(X, len(grumpy) + 1))

    def maxSatisfied(self, customers: List[int],
                     grumpy: List[int], X: int) -> int:
        default = sum(c for g, c in zip(grumpy, customers) if g == 0)
        addable = sum(c for g, c in zip(grumpy[:X], customers[:X]) if g == 1)
        mx = addable

        for i in range(X, len(customers)):
            addable += customers[i] * grumpy[i]
            addable -= customers[i - X] * grumpy[i - X]
            mx = max(mx, addable)
        return default + mx


def test():
    sol = Solution()
    cases = [
        ([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3),
        ([1], [0], 1),
        ([3, 7], [0, 0], 2),
        ([2, 6, 6, 9], [0, 0, 1, 1], 1),
    ]
    for case in cases:
        print(sol.maxSatisfied(*case))  # 16 1 10 17


if __name__ == '__main__':
    test()
