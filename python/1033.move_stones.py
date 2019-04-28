from typing import List

class Solution:
    def numMovesStones(self, a:int, b:int, c:int) -> List[int]:
        a, b, c = sorted([a, b, c])
        minimum = 0
        maximum = 0
        for i in range(a + 1, c):
            if i == b:
                continue
            maximum += 1
        d1 = b - a
        d2 = c - b
        if d1 == 2 or d2 == 2:
            minimum = 1
        elif d1 > 1 and d2 > 1:
            minimum  = 2
        elif d1 > 1 or d2 > 1:
            minimum = 1
        return [minimum, maximum]


def test():
    s = Solution()
    print(s.numMovesStones(1, 2, 5))
    print(s.numMovesStones(4, 3, 2))
    print(s.numMovesStones(4, 3, 2))
    print(s.numMovesStones(2, 4, 1))
    print(s.numMovesStones(7, 4, 1))
    print(s.numMovesStones(3, 5, 1))
    print(s.numMovesStones(1, 3, 6))


if __name__ == '__main__':
    test()
