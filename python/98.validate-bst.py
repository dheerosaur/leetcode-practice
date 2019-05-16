"""
Given a binary tree, determine if it is a valid binary search tree (BST)

"""
from ds.bst import TreeNode, constructBST


class BadQueue:
    """
    Suboptimal queue just for testing
    """
    def __init__(self):
        self._q = []

    def enqueue(self, k):
        self._q.insert(0, k)

    def dequeue(self):
        return self._q.pop()

    def is_empty(self):
        return len(self._q) == 0


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        lvalid = rvalid = True
        if root.left:
            lvalid = root.left.val < root.val \
                and self.isValidBST(root.left)
        if root.right:
            rvalid = root.right.val > root.val \
                and self.isValidBST(root.right)
        return lvalid and rvalid

    def isValidBST2(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True
        return helper(root)

    def isValidBST_iter(self, root: TreeNode) -> bool:
        queue = BadQueue()
        queue.enqueue(root)
        while not queue.is_empty():
            node = queue.dequeue()
            if node is None:
                continue
            if node.left is not None:
                if node.left.val > node.val:
                    return False
            if node.right is not None:
                if node.right.val < node.val:
                    return False
            queue.enqueue(node.left)
            queue.enqueue(node.right)
        return True


def test():
    sol = Solution()
    valid_cases = [
        constructBST([2, 1, 3]),
        constructBST([5, 3, 7, 2, 4, 6, 8, 1])
    ]
    invalid_cases = [
        constructBST([5, 1, 6, None, None, 7, 8]),
        constructBST([1, 2, 3, 4, 5, 6, 7, 9])
    ]
    methods = ['isValidBST', 'isValidBST2', 'isValidBST_iter']
    for method in methods:
        func = getattr(sol, method)
        for case in valid_cases:
            assert func(case) is True
        for case in invalid_cases:
            assert func(case) is False


if __name__ == '__main__':
    test()
