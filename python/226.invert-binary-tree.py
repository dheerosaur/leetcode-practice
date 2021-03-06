#
# @lc app=leetcode id=226 lang=python3
# [algorithms] - Easy
#
# [226] Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/
#
# Invert a binary tree.
#
# Example:
#
# Input:
#
#
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
#
# Output:
#
#
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
#
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you
# can’t invert a binary tree on a whiteboard so f*** off.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from ds.bst import TreeNode, traverse, constructBST


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            right, left = root.right, root.left
            root.left = self.invertTree(right)
            root.right = self.invertTree(left)
        return root


def test():
    sol = Solution()
    cases = [
        constructBST([1, 2, 3, 4, 5, 6, 7]),
    ]
    for case in cases:
        print(traverse(sol.invertTree(case)))


if __name__ == '__main__':
    test()
