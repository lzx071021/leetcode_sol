"""Leetcode #268 缺失的数字"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        checker = {i: 0 for i in range(n+1)}
        for digit in nums:
            checker[digit] += 1
        for key, value in checker.items():
            if value == 0:
                return key
        return -1

    def linear_missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = sum([i for i in range(n+1)])
        for digit in nums:
            expected_sum -= digit
        return expected_sum


sol = Solution()
nums = [3, 0, 1]  # Expected: 2
nums1 = [9, 6, 4, 3, 0, 1, 2, 5, 7]  # Expected: 8
print(sol.missingNumber(nums))
print(sol.missingNumber(nums1))
