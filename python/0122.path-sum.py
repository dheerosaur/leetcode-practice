from ds.bst import TreeNode, constructBST


class Solution:
    def hasPathSum_1(self, root: TreeNode, total: int) -> bool:

        def helper(node, sofar):
            if node.left is None and node.right is None:
                return total == (sofar + node.val)
            result = False
            if node.left:
                result = result or helper(node.left, sofar + node.val)
            if node.right:
                result = result or helper(node.right, sofar + node.val)
            return result

        if root is None:
            return False
        return helper(root, 0)

    def hasPathSum(self, root: TreeNode, total: int) -> bool:
        if root is None:
            return False

        total = total - root.val

        if root.left is None and root.right is None:
            return total == 0

        return self.hasPathSum(root.left, total) \
            or self.hasPathSum(root.right, total)


def main():
    sol = Solution()
    cases = [
        ([1, 2], 1),
        ([1, 2, 2, 3, None, None, None, 3], 9),
        ([1, 2, 2, 3, 9, 9, 3], 6),
        ([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5], 30),
    ]
    for ls, total in cases:
        tree = constructBST(ls)
        print(sol.hasPathSum(tree, total))


if __name__ == '__main__':
    main()
