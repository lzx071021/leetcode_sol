"""Leetcode #283 移动零"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Bad Implementation !
        """

        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                for j in range(i+1, length):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break


test_case = {
    [0, 1, 0, 3, 12]: [1, 3, 12, 0, 0]
}
