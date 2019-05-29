"""
Given a string S of lowercase letters, a duplicate removal consists of choosing
two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It
is guaranteed the answer is unique.

"""


class Solution:

    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


def test():
    sol = Solution()
    cases = [
        "",
        "a",
        "aa",
        "abbaca",
        "abbccddefghijjkkil",
    ]
    for case in cases:
        print(sol.removeDuplicates(case))
        # assert sol.removeDuplicates() == sol.removeDuplicates_2()


if __name__ == '__main__':
    test()
