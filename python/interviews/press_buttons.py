
class Solution:
    kb = None

    def go(self, c, x1, y1):
        path = []
        x2, y2 = self.kb[c]
        dx, dy = x2 - x1, y2 - y1
        while dx < 0:
            dx += 1
            path.append('U')
        while dx > 0:
            dx -= 1
            path.append('D')
        while dy < 0:
            dy += 1
            path.append('L')
        while dy > 0:
            dy -= 1
            path.append('R')
        return ''.join(path)

    def press(self, output: str) -> str:
        result = []
        x1, y1 = 0, 0

        for c in output:
            result.append(self.go(c, x1, y1))
            result.append('E')
            x1, y1 = self.kb[c]
        return ''.join(result)


keyboard_string = """
ABCDEFGHIJ
KLMNOPQRS
TUVWXYZ"""


def get_keyboard(s):
    rows = s.strip().split()
    return {s: (i, j)
            for i, row in enumerate(rows)
            for j, s in enumerate(row)}


def test():
    sol = Solution()
    sol.kb = get_keyboard(keyboard_string)
    print(sol.kb)
    cases = [
        'BATMAN'
    ]
    for case in cases:
        print(sol.press(case))


if __name__ == '__main__':
    test()
