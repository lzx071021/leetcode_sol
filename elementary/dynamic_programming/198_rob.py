"""Leetcode #198 打家劫舍"""

from typing import List
from collections import defaultdict


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        p = defaultdict(lambda: defaultdict(lambda: 0))
        for i in range(1, n+1):
            p[i][i] = nums[i-1]
        for l in range(2, n+1):
            for i in range(1, n-l+2):
                j = i + l - 1
                for k in range(i, j+1):
                    p[i][j] = max(p[i][j], p[i][k-1] + p[k+1][j])
        return p[1][n]


sol = Solution()
nums = [2, 7, 9, 3, 1]
nums1 = [1, 2, 3, 1]
nums2 = [2, 3, 2]
print(sol.rob(nums))
print(sol.rob(nums1))
print(sol.rob(nums2))
