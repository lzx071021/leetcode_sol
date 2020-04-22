"""Leetcode #70 爬楼梯"""

from collections import defaultdict


class Solution:
    def climbStairs(self, n: int) -> int:
        m = defaultdict(lambda: 1)
        for i in range(2, n+1):
            m[i] = m[i-1] + m[i-2]
        return m[n]


sol = Solution()
print(sol.climbStairs(6))
