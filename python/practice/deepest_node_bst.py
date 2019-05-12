"""
Given the root to a binary tree, return the deepest node.
"""
from ds.bst import TreeNode, constructBST


class Solution:

    def deepest(self, root: TreeNode) -> TreeNode:
        max_depth = 0
        dnodes = []

        def helper(node, depth=0):
            nonlocal max_depth, dnodes
            if node is not None:
                helper(node.right, depth + 1)
                helper(node.left, depth + 1)
                if depth == max_depth:
                    dnodes.append(node)
                if depth > max_depth:
                    max_depth = depth
                    dnodes = [node]
        helper(root)
        return dnodes


def test():
    sol = Solution()
    cases = [
        [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    ]
    for case in cases:
        tree = constructBST(case)
        dnodes = sol.deepest(tree)
        print([d.val for d in dnodes])
        # assert sol.bstToGst() == sol.bstToGst_2()


if __name__ == '__main__':
    test()
