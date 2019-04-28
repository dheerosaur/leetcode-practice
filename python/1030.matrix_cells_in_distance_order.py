from typing import List
from collections import defaultdict


class Solution:
    def allCellsDistOrder(self, R:int, C:int, r0:int, c0:int) -> List[List[int]]:
        hmap = defaultdict(list)
        for i in range(R):
            for j in range(C):
                distance = abs(r0 - i) + abs(c0 - j)
                hmap[distance].append([i, j])
        result = []
        for k in sorted(hmap):
            result.extend(hmap[k])
        return result


def test():
    s = Solution()
    print(s.allCellsDistOrder(1, 2, 0, 0))
    print(s.allCellsDistOrder(2, 2, 0, 1))
    print(s.allCellsDistOrder(2, 3, 1, 2))


test()
