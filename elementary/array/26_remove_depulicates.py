"""Leetcode #26 删除排序数组中的重复项"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1


test_case = {
    [1, 1, 2], 2,
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5
}
