"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.
"""

from ds.bst import TreeNode, constructBST


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        count = [0]

        def helper(node):
            if node is None:
                return True

            left = helper(node.left)
            right = helper(node.right)

            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False

            if left and right:
                count[0] += 1
                return True

            return False

        helper(root)
        return count[0]


def main():
    sol = Solution()
    cases = [
        [1, 0],
        [5, 1, 5, 5, 5, None, 5],
        [5, 5, 5, 5, 5, 5, 5],
    ]
    for case in cases:
        tree = constructBST(case)
        print(sol.countUnivalSubtrees(tree))


if __name__ == '__main__':
    main()
