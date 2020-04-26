"""Leetcode #384 打乱数组"""
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.nums.copy()
        return self.insertion_sort(nums, self.generate_priority(nums))

    def generate_priority(self, nums):
        n = len(nums)
        priority = [i for i in range(n)]
        for i in range(n):
            j = random.randint(i, n-1)
            priority[i], priority[j] = priority[j], priority[i]
        return priority

    def insertion_sort(self, nums, priority):
        n = len(nums)
        for j in range(1, n):
            key = nums[j]
            priority_key = priority[j]
            i = j - 1
            while i >= 0 and priority[i] >= priority_key:
                nums[i+1] = nums[i]
                priority[i+1] = priority[i]
                i -= 1
            nums[i+1] = key
            priority[i+1] = priority_key
        return nums


nums = [1, 2, 3, 4]
p = [36, 3, 62, 19]
sol = Solution(nums)
# print(sol.generate_priority(nums))
print(sol.nums)
print(sol.shuffle())
print(sol.reset())

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
