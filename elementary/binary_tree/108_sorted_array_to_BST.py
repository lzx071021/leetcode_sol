"""Leetcode #108 将有序数组转换为二叉树"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left, root.right = map(self.sortedArrayToBST, [
                                    nums[:mid], nums[mid+1:]])
        return root


test_case = {
    [-10, -3, 0, 5, 9]: [0, -3, 9, -10, None, 5]  # A possible answer
}
