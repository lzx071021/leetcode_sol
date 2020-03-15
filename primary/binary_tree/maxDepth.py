# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node(val: %s, left: %s, right: %s)' % (self.val, self.left, self.right)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth_dict = {}

        def forward(node, depth):
            depth_dict[node] = depth
            self_depth = depth + 1
            if node.left:
                forward(node.left, self_depth)
            if node.right:
                forward(node.right, self_depth)

        forward(root, 1)
        max_depth = 0
        for depth in depth_dict.values():
            if depth > max_depth:
                max_depth = depth
        return max_depth


root = TreeNode(3)
lt, rt = TreeNode(9), TreeNode(20)
root.left, root.right = lt, rt
lt, rt = TreeNode(15), TreeNode(7)
root.right.left, root.right.right = lt, rt

sol = Solution()
print(sol.maxDepth(root))
