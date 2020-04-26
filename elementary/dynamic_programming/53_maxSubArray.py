"""Leetcode #53 最大子序和"""

from typing import List
from collections import defaultdict


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = defaultdict(lambda: float('-inf'))
        for i in range(len(nums)):
            m[i] = max(nums[i], m[i-1] + nums[i])
        return max(m.values())


sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sol.maxSubArray(nums))
