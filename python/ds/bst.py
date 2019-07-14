"""
Implementing some basic BS functionality
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traverse(root):
    "inorder traversal for testing"
    if root is None:
        return
    traverse(root.left)
    print(root.val, end=' ')
    traverse(root.right)


def _bfs(root):
    result = []
    q = [root]
    while q:
        node = q.pop()
        if node is not None:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
    return result


def constructBST(vals, i=0):
    if i < len(vals) and vals[i] is not None:
        root = TreeNode(vals[i])
        root.left = constructBST(vals, 2 * i + 1)
        root.right = constructBST(vals, 2 * i + 2)
        return root
    return None


def test():
    traverse(constructBST([2, 1, 3]))
    print()
    traverse(constructBST([5, 1, 7, None, None, 6, 8]))
    print()
    traverse(constructBST([5, 3, 7, 2, 4, 6, 8, 1]))
    print()


if __name__ == '__main__':
    test()
