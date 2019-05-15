# @lc app=leetcode id=101 lang=python3
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
from collections import deque
from ds.bst import TreeNode, constructBST


class Solution:
    def isSymmetric_recur(self, root: TreeNode) -> bool:
        def helper(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (t1.val == t2.val and
                    helper(t1.left, t2.right) and
                    helper(t1.right, t2.left))
        return helper(root, root)

    def isSymmetric(self, root: TreeNode) -> bool:
        "Do BFS and at each level, compare q to reverse"
        dq = deque([(root, root)])

        while dq:
            ll, rr = dq.popleft()
            if (ll is None and rr is None):
                continue
            if (ll is None or rr is None) or (ll.val != rr.val):
                return False
            dq.append((ll.left, rr.right))
            dq.append((ll.right, rr.left))
        return True


def main():
    sol = Solution()
    cases = [
        [1, 0],
        [1, 2, 2, 3, None, None, None, 3],
        [1, 2, 2, 3, 4, 4, 3],
        [1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5],
    ]
    for case in cases:
        tree = constructBST(case)
        print(sol.isSymmetric(tree))


if __name__ == '__main__':
    main()
