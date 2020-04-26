"""Leetcode #136 只出现一次的数字"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = {}
        for num in nums:
            if num not in visited:
                visited[num] = 1
            else:
                visited.pop(num)
        return visited.popitem()[0]


test_case = {
    [2, 2, 1]: 1,
    [4, 1, 2, 1, 2]: 4
}
