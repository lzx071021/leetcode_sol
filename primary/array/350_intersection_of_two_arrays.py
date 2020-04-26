"""Leetcode #350 两个数组的交集 II"""
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Hash table"""

        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        inter_set = [ele for ele in (cnt1 & cnt2).elements()]
        return inter_set


test_case = {
    ([1, 2, 2, 1], [2, 2]): [2, 2],
    ([4, 9, 5], [9, 4, 9, 8, 4]): [4, 9]
}
