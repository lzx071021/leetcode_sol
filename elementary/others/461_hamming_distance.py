"""Leetcode #461 汉明距离"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x or y:
            if x & 1 != y & 1:
                cnt += 1
            x >>= 1
            y >>= 1
        return cnt


sol = Solution()
print(sol.hammingDistance(1, 4))  # Expected: 2
