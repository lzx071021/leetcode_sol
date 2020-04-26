"""Leetcode #1 两数之和"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_dict = {}

        for idx, num in enumerate(nums):
            if target - num in num_idx_dict:
                return [num_idx_dict[target-num], idx]
            num_idx_dict[num] = idx


test_case = {
    ([2, 7, 11, 15], 9): [0, 1]
}
