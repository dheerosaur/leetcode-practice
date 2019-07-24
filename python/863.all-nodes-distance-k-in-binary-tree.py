#
# @lc app=leetcode id=863 lang=python3
# [algorithms] - Medium
#
# [863] All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# We are given a binary tree (with root node root), a target node, and an
# integer value K.
#
# Return a list of the values of all nodes that have a distance K from the
# target node.  The answer can be returned in any order.
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
#
# Output: [7,4,1]
#
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
#
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these
# objects.
#
# Note:
#
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
from ds.bst import TreeNode, constructBST


class Solution:
    result = []

    def distanceK_bfs_bfs(self, root: TreeNode, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        visited = set()
        q = collections.deque([root])
        while q:
            node = q.popleft()
            visited.add(node.val)
            for n in (node.left, node.right):
                if n and n.val not in visited:
                    q.append(n)
                    graph[n.val].add(node.val)
                    graph[node.val].add(n.val)

        self.result = []

        def bfs(g, src):
            q, d = collections.deque(), 0
            q.append((src, d))
            visited = set()
            while q and d <= K:
                node, d = q.popleft()
                visited.add(node)
                if d == K:
                    self.result.append(node)
                for n in g[node]:
                    if n not in visited:
                        q.append((n, d + 1))

        bfs(graph, target)
        return self.result

    def distanceK_dfs_bfs(self, root: TreeNode, target, K):
        graph = collections.defaultdict(list)

        def connect(parent, child):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)

        connect(None, root)
        bfs = [target]
        seen = set(bfs)
        for _ in range(K):
            bfs = [y for x in bfs for y in graph[x] if y not in seen]
            seen |= set(bfs)
        return bfs

    def distanceK(self, root: TreeNode, target, K):
        graph, visited = collections.defaultdict(list), set()

        def add_edges(u, v):
            graph[u.val].append(v.val)
            graph[v.val].append(u.val)

        def dfs(node):
            if node.left:
                add_edges(node, node.left)
                dfs(node.left)
            if node.right:
                add_edges(node, node.right)
                dfs(node.right)

        dfs(root)
        result = []

        def find(node, d):
            if d < K:
                visited.add(node)
                for v in graph[node]:
                    if v not in visited:
                        find(v, d + 1)
            else:
                result.append(node)

        find(target, 0)
        return result


def test():
    sol = Solution()
    cases = [
        # Tree as nodes
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 4, 2),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 2),
    ]
    for case in cases:
        tree, *rest = case
        print(sol.distanceK(constructBST(tree), *rest))


if __name__ == "__main__":
    test()
