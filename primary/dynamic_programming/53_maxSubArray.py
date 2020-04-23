"""Leetcode #53 最大子序和"""

from typing import List
from collections import defaultdict


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(lambda: 0)
        # max_sum = float('-inf')
        for i in range(n):
            m[i] = max(nums[i], m[i-1] + nums[i])
            # max_sum = max(max_sum, m[i])
        # return max_sum
        return max(m.values())


sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sol.maxSubArray(nums))
