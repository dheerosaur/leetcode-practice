from typing import List


class Solution:
    edges = 0

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graph = {i: set() for i in range(n)}

        for i in range(n):
            for j in range(n):
                x1, y1 = stones[i]
                x2, y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    graph[i].add(j)
                    graph[j].add(i)

        def dfs(s):
            visited.add(s)
            for n in graph[s]:
                if n not in visited:
                    self.edges += 1
                    dfs(n)

        visited = set()
        total_edges = 0
        for i in range(n):
            if i not in visited:
                self.edges = 0
                dfs(i)
                total_edges += self.edges
        return total_edges


def test():
    sol = Solution()
    cases = [
        [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]],
        [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]],
    ]
    for case in cases:
        print(sol.removeStones(case))


if __name__ == "__main__":
    test()
