"""Leetcode #101 对称二叉树"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node(val: %s, left: %s, right: %s)' % (self.val, self.left, self.right)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        nodes = []

        def inorder_walk(node, pos=None):
            if node:
                inorder_walk(node.left, 'lt')
                # ! Why would pos be like this when dealing with root node?
                nodes.append((node.val, pos))
                inorder_walk(node.right, 'rt')

        inorder_walk(root, nodes)
        p, q = 0, len(nodes) - 1
        while p < q:
            if nodes[p][0] != nodes[q][0] or nodes[p][1] == nodes[q][1]:
                return False
            p, q = p + 1, q - 1
        return True


# root = TreeNode(1)
# lt, rt = TreeNode(2), TreeNode(2)
# root.left, root.right = lt, rt
# lt, rt = TreeNode(3), TreeNode(4)
# root.left.left, root.left.right = lt, rt
# lt, rt = TreeNode(4), TreeNode(3)
# root.right.left, root.right.right = lt, rt

root = TreeNode(1)
lt, rt = TreeNode(2), TreeNode(2)
root.left, root.right = lt, rt
root.left.left = TreeNode(2)
root.right.left = TreeNode(2)

sol = Solution()
print(sol.isSymmetric(root))
