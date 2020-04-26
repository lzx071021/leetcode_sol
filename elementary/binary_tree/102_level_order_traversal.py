"""Leetcode #102 二叉树层次遍历"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        record = {}

        def inorder_walk(node, depth=0):
            if node:
                inorder_walk(node.left, depth=depth+1)
                record[depth] = record.setdefault(depth, []) + [node.val]
                inorder_walk(node.right, depth=depth+1)

        inorder_walk(root)
        res = [record[key] for key in sorted(record.keys())]
        return res


test_case = {
    [3, 9, 20, None, None, 15, 7]:
    [
        [3],
        [9, 20],
        [15, 7]
    ]
}
