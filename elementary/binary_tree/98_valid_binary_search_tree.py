"""Leetcode #98 验证二叉搜索树"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node(val: %s, left: %s, right: %s)' % (self.val, self.left, self.right)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nodes_record = []

        def inorder(node, nodes_record):
            if node:
                inorder(node.left, nodes_record)
                nodes_record.append(node.val)
                inorder(node.right, nodes_record)

        inorder(root, nodes_record)
        if sorted(nodes_record) == nodes_record and len(set(nodes_record)) == len(nodes_record):
            return True
        else:
            return False


sol = Solution()

root = TreeNode(5)
lt, rt = TreeNode(1), TreeNode(7)
root.left, root.right = lt, rt
lt, rt = TreeNode(3), TreeNode(6)
root.right.left, root.right.right = lt, rt
print(sol.isValidBST(root))

# root1 = TreeNode(2)
# lt, rt = TreeNode(1), TreeNode(3)
# root1.left, root1.right = lt, rt
# print(sol.isValidBST(root1))
