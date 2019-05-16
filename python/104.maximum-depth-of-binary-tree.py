# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
from ds.bst import TreeNode, constructBST


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node):
            if node is None:
                return 0
            ldepth = helper(node.left)
            rdepth = helper(node.right)
            return 1 + max(ldepth, rdepth)
        return helper(root)


def main():
    sol = Solution()
    cases = [
        [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
        [40, 20, 60, 12, 32, None, None],
        range(31),
        range(32),
    ]
    for case in cases:
        tree = constructBST(case)
        print(sol.maxDepth(tree))


if __name__ == '__main__':
    main()
