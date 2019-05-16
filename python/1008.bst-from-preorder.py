"""
Return the root node of a binary search tree that matches the given
preorder traversal.

"""
from typing import List
from ds.bst import traverse, TreeNode


class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(lower=float('-inf'), upper=float('inf')):
            nonlocal idx
            if idx == n:
                return None
            val = preorder[idx]

            if val < lower or val > upper:
                return None

            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        idx = 0
        n = len(preorder)
        return helper()

    def bstFromPreorder_iter(self, preorder: List[int]) -> TreeNode:
        n = len(preorder)
        if not n:
            return None

        root = TreeNode(preorder[0])
        stack = [root, ]

        for i in range(1, n):
            node, child = stack[-1], TreeNode(preorder[i])
            while stack and stack[-1].val < child.val:
                node = stack.pop()

            if child.val > node.val:
                node.right = child
            else:
                node.left = child
            stack.append(child)
        return root


def test():
    sol = Solution()
    cases = [
        [8, 5, 1, 6, 10],
        [8, 5, 1, 12, 10, 11, 13],
    ]
    for case in cases:
        traverse(sol.bstFromPreorder(case))
        print()
        traverse(sol.bstFromPreorder_iter(case))
        print()
        # assert sol.bstFromPreorder() == sol.bstFromPreorder_2()


if __name__ == '__main__':
    test()
