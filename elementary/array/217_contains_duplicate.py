"""Leetcode #217 存在重复元素"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """用字典记录已经访问过的元素"""

        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False


test_case = {
    [1, 2, 3, 1]: True,
    [1, 2, 3, 4]: False
}
