#
# @lc app=leetcode id=653 lang=python3
# [algorithms] - Easy
#
# [653] Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# Given a Binary Search Tree and a target number, return true if there exist
# two elements in the BST such that their sum is equal to the given target.
#
# Input:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
# Input:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 28
#
# Output: False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from ds.bst import TreeNode, constructBST


class Solution:
    def findTarget_dfs(self, root: TreeNode, k: int) -> bool:
        def find(root):
            if root is None:
                return False
            if root.val in s:
                return True
            s.add(k - root.val)
            return find(root.left) or find(root.right)

        s = set()
        return find(root)

    def findTarget_bfs(self, root: TreeNode, k: int) -> bool:
        s = set()
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if k - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        return False

    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(root):
            if root:
                inorder(root.left)
                A.append(root.val)
                inorder(root.right)

        A = []
        inorder(root)

        left, right = 0, len(A) - 1
        while left < right:
            total = A[left] + A[right]
            if total == k:
                return True
            elif total > k:
                right -= 1
            else:
                left += 1
        return False


def test():
    sol = Solution()
    cases = [
        ([5, 3, 6, 2, 4, None, 7], 9),
        ([5, 3, 6, 2, 4, None, 7], 22),
    ]
    for T, k in cases:
        print(sol.findTarget(constructBST(T), k))


if __name__ == '__main__':
    test()
