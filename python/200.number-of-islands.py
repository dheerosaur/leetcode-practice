#
# @lc app=leetcode id=200 lang=python3
# [algorithms] - Medium
#
# [200] Number of Islands
# https://leetcode.com/problems/number-of-islands/description/
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # We have to find the number of connected components
        # We do dFS from all nodes while marking visited nodes in a set
        m, n = len(grid), len(grid[0])
        visited = set()
        components = []

        def neighbors(i, j):
            positions = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
            for x, y in positions:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                    yield x, y

        def dfs(i, j):
            num_items = 0
            q = [(i, j)]
            while q:
                x, y = q.pop()
                if (x, y) not in visited:
                    visited.add((x, y))
                    num_items += 1
                    for x1, y1 in neighbors(x, y):
                        q.append((x1, y1))
            components.append(num_items)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)

        return components


def test():
    sol = Solution()
    cases = [
        # cases
        [list(s) for s in "11110,11010,11000,00000".split(",")],
        [list(s) for s in "11000,11000,00100,00011".split(",")],
    ]
    for case in cases:
        print(sol.numIslands(case))


if __name__ == "__main__":
    test()
