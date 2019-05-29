# Distant barcodes

import time
import collections
from typing import List


class Solution:

    def rearrangeBarcodes(self, A: List[int]) -> List[int]:
        mid = len(A) // 2
        count = collections.Counter(A)
        A.sort(key=lambda a: (count[a], a))
        A[1::2], A[::2] = A[:mid], A[mid:]
        return A

    def rearrangeBarcodes2(self, A: List[int]) -> List[int]:
        i, n = 0, len(A)
        res = [0] * n
        for k, v in collections.Counter(A).most_common():
            for _ in range(v):
                res[i] = k
                i += 2
                if i >= n:
                    i = 1
        return res


cases = [
    [1, 1, 2],
    [1, 2, 2],
    [1, 2, 2, 3, 3],
    [4, 3, 8, 4, 4, 4, 8, 3, 3, 3]
]


def test():
    sol = Solution()
    for case in cases:
        print(sol.rearrangeBarcodes(case))


def speed_test(method, times):
    start = time.time()
    method = getattr(Solution(), method)
    for _ in range(times):
        for case in cases:
            method(case)
    secs = (time.time() - start) / 1000
    print(secs)


if __name__ == '__main__':
    test()
    #  speed_test('rearrangeBarcodes', 1000)
    #  speed_test('rearrangeBarcodes2', 1000)
