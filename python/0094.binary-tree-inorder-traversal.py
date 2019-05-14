#
# @lc app=leetcode id=94 lang=python3
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from ds.bst import TreeNode, constructBST


class Solution:
    def inorderTraversal_Recur(self, root: TreeNode) -> List[int]:
        result = []

        def helper(node):
            nonlocal result
            if node is not None:
                helper(node.left)
                result.append(node.val)
                helper(node.right)

        helper(root)
        return result

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        node = root
        while node or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right()

        return result


def test():
    sol = Solution()
    cases = [
        [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    ]
    for case in cases:
        tree = constructBST(case)
        print(sol.inorderTraversal(tree))


if __name__ == '__main__':
    test()
