from typing import List
from ds.bst import TreeNode, constructBST


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        def bfs(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)

            if node.left:
                bfs(node.left, level + 1)
            if node.right:
                bfs(node.right, level + 1)

        bfs(root, 0)
        return result


def test():
    sol = Solution()
    cases = [
        [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
        [40, 20, 60, 12, 32, None, None],
    ]
    for case in cases:
        tree = constructBST(case)
        print(sol.levelOrder(tree))


if __name__ == '__main__':
    test()
