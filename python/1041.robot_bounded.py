"""

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The
robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.

The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the
robot never leaves the circle.

"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        x, y = (0, 0)
        changes = {'G': 0, 'L': 90, 'R': -90}
        for c in instructions:
            direction = (direction + changes[c]) % 360
            if c == 'G':
                if direction == 0:
                    x += 1
                elif direction == 90:
                    y -= 1
                elif direction == 180:
                    x -= 1
                else:
                    y += 1
        if (x, y) == (0, 0):
            return True
        return (direction % 360) != 0


def test():
    sol = Solution()
    cases = [
        "GGLLGG",
        "GG",
        "GL",
        "LRRRRLLLRL",
        "GGRGGRGGRGGR",
    ]
    for case in cases:
        print(sol.isRobotBounded(case))
        # assert sol.isRobotBounded() == sol.isRobotBounded_2()


if __name__ == '__main__':
    test()
