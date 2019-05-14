#
# @lc app=leetcode id=783 lang=python3
#
#
# Given a Binary Search Tree (BST) with the root node root, return the minimum
# difference between the values of any two different nodes in the tree.
#
# Example :
#
#
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
#
# The given tree [4,2,6,1,3,null,null] is represented by the following
# diagram:
#
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \
# ⁠   1   3
#
# while the minimum difference in this tree is 1, it occurs between node 1 and
# node 2, also between node 3 and node 2.
#
#
# Note:
#
#
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's
# value is different.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from ds.bst import TreeNode, constructBST


class Solution:

    def __init__(self):
        self.prev = float('-inf')
        self.min = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        "without nonlocal variable. Use parameter"
        def inorder(node):
            if node is not None:
                inorder(node.left)
                self.min = min(self.min, node.val - self.prev)
                self.prev = node.val
                inorder(node.right)
        inorder(root)
        return self.min


def test():
    sol = Solution()
    cases = [
        [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
        [40, 20, 60, 12, 32, None, None],
    ]
    for case in cases:
        tree = constructBST(case)
        print(sol.minDiffInBST(tree))


if __name__ == '__main__':
    test()
