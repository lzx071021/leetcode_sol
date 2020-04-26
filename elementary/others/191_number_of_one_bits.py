"""Leetcode #191 位1的个数"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            if n & 1:
                cnt += 1
            n >>= 1
        return cnt

    def hammingWeight2(self, n: int) -> int:
        cnt = 0
        while n:
            n &= (n-1)
            cnt += 1
        return cnt


sol = Solution()
print(sol.hammingWeight(11))  # Expected: 3
print(sol.hammingWeight2(11))  # Expected: 3
