from ds.bst import TreeNode, constructBST


class Solution:
    def lca(self, root: TreeNode, a: int, b: int) -> int:
        def helper(root):
            if root is None:
                return False
            if root.val in (a, b):
                return root
            left = helper(root.left)
            right = helper(root.right)
            if left and right:
                return root
            return left or right

        return helper(root).val


def main():
    sol = Solution()
    root = constructBST([1, 2, 3, 4, 5, 6, 7, 8])
    cases = [
        (root, 4, 5),
        (root, 4, 8),
        (root, 5, 8),
        (root, 3, 7),
        (root, 7, 8)
        # test cases
    ]
    for case in cases:
        print(sol.lca(*case))


if __name__ == "__main__":
    main()
