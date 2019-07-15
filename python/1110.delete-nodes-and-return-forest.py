from typing import List
from ds.bst import TreeNode, _bfs, constructBST


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_remove = set(to_delete)

        def dfs(node, parent=None):
            if node is None:
                return
            elif node.val in to_remove:
                if parent and parent.left is node:
                    parent.left = None
                if parent and parent.right is node:
                    parent.right = None
                dfs(node.left)
                dfs(node.right)
            else:
                if parent is None:
                    ans.append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return ans

    def delNodes_alt(self, root: TreeNode, to_delete) -> List[TreeNode]:
        ans = []
        to_remove = set(to_delete)

        def dfs(root, parent_deleted):
            if root is None:
                return None
            current_deleted = root.val in to_remove
            if parent_deleted and not current_deleted:
                ans.append(root)
            root.left = dfs(root.left, current_deleted)
            root.right = dfs(root.right, current_deleted)
            return None if current_deleted else root

        dfs(root, True)
        return ans


def test():
    sol = Solution()
    cases = [(constructBST([1, 2, 3, 4, 5, 6, 7]), [3, 5])]
    for case in cases:
        for root in sol.delNodes(*case):
            print(_bfs(root))


test()
