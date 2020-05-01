"""Leetcode #334 递增的三元子序列 https://leetcode-cn.com/problems/increasing-triplet-subsequence/"""
from typing import List, Tuple


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minimum, penultimate = float('inf'), float('inf')
        for num in nums:
            # * The first two cmp must be <= so that the last implicit is always strict >
            if num <= minimum:
                minimum = num
            elif num <= penultimate:
                penultimate = num
            else:
                return True if len(nums) >= 3 else False
        return False

    def my_increasingTriplet(self, nums: List[int]) -> bool:
        # TODO To be implemented with the aid of find_minimal_with_dix: do few times of traversal.

        return False

    def find_minimal_with_idx(self, nums: List[int], base: int) -> Tuple[int, int]:
        minimal = None
        idx_of_min = 0
        for idx, num in enumerate(nums):
            if num < base:
                minimal = num
                idx_of_min = idx
        return minimal, idx_of_min


test_case = [0, 4, 2, 1, 0, -1, -3]
test_case0 = [5, 4, 6, 3, 7, 2, 8]
test_case1 = [1, 2, 3, 4, 5]
test_case2 = [5, 4, 3, 2, 1]

sol = Solution()
print(sol.increasingTriplet(test_case))
print(sol.increasingTriplet(test_case0))
print(sol.increasingTriplet(test_case1))
print(sol.increasingTriplet(test_case2))
