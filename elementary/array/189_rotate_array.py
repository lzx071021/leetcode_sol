"""Leetcode #189 旋转数组"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


test_case = {
    ([1, 2, 3, 4, 5, 6, 7], 7): [5, 6, 7, 1, 2, 3, 4],
    ([-1, -100, 3, 9], 2): [3, 99, -1, -100]
}
