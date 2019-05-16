from typing import List
from ds.bst import TreeNode


class Solution:
    def preorderTraversal_Recur(self, root: TreeNode) -> List[int]:
        result = []

        def traverse(node):
            nonlocal result
            if node is not None:
                result.append(node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return result

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, result = [root], []

        while stack:
            root = stack.pop()
            if root is not None:
                result.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return result
