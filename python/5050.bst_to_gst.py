"""
Given the root of a binary search tree with distinct values, modify it so that
every node has a new value equal to the sum of the values of the original tree
that are greater than or equal to node.val.
"""
from ds.bst import TreeNode, constructBST, traverse


class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(node):
            nonlocal total
            if node is not None:
                helper(node.right)
                node.val = total = total + node.val
                helper(node.left)
        total = 0
        helper(root)
        return root


def test():
    sol = Solution()
    cases = [
        [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    ]
    for case in cases:
        tree = constructBST(case)
        traverse(sol.bstToGst(tree))
        # assert sol.bstToGst() == sol.bstToGst_2()


if __name__ == '__main__':
    test()
