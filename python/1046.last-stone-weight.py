from typing import List
import bisect
import heapq


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]  # to make it a max heapq
        heapq.heapify(pq)
        while len(pq) > 1:
            s1 = heapq.heappop(pq)
            s2 = heapq.heappop(pq)
            if s1 - s2:
                heapq.heappush(pq, -abs(s1 - s2))
        return -pq[0] if pq else 0

    def lastStoneWeight_n2(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            *stones, small, large = stones
            bisect.insort(stones, large - small)
        return stones[0]


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
