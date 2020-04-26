"""Leetcode #326 3的幂"""

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        res = math.log(n, 3)
        return n == 3**round(res)


sol = Solution()
print(sol.isPowerOfThree(0))
print(sol.isPowerOfThree(27))
print(sol.isPowerOfThree(243))
