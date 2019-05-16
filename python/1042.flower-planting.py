"""
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of
4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x
to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two
gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of
flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3,
or 4.  It is guaranteed an answer exists.


Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
"""
from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        G = [[] for _ in range(N)]
        result = [0] * N
        colors = {1, 2, 3, 4}

        for u, v in paths:
            G[u - 1].append(v - 1)
            G[v - 1].append(u - 1)

        for i in range(N):
            legal_colors = colors - {result[v] for v in G[i]}
            result[i] = legal_colors.pop()
        return result

    def gardenNoAdj_fill(self, N: int, paths: List[List[int]]) -> List[int]:
        g = [set() for _ in range(N)]  # graph
        result = [0] * N
        colors = (1, 2, 3, 4)

        # Construct graph
        for u, v in paths:
            u, v = u - 1, v - 1
            g[u].add(v)
            g[v].add(u)

        for i in range(N):
            fill = [0, 0, 0, 0, 0]

            for v in g[i]:
                if result[v]:
                    fill[result[v]] = 1

            for color in colors:
                if not fill[color]:
                    result[i] = color
                    break

        return result


def test():
    sol = Solution()
    cases = [
        (3, [[1, 2], [2, 3], [3, 1]]),
        (4, [[1, 2], [3, 4]]),
        (4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]),
    ]
    for case in cases:
        print(sol.gardenNoAdj(*case))
        # assert sol.gardenNoAdj() == sol.gardenNoAdj_2()


if __name__ == '__main__':
    test()
