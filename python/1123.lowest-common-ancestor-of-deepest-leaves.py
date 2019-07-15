from ds.bst import TreeNode, constructBST


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if root is None:
                return 0, None
            d1, anc1 = helper(root.left)
            d2, anc2 = helper(root.right)
            if d1 > d2:
                node = anc1
            elif d1 < d2:
                node = anc2
            else:
                node = root
            return max(d1, d2) + 1, node

        depth, node = helper(root)
        return depth, node.val


def test():
    sol = Solution()
    cases = [
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6, 7],
    ]
    for case in cases:
        root = constructBST(case)
        print(case, sol.lcaDeepestLeaves(root))


if __name__ == "__main__":
    test()
