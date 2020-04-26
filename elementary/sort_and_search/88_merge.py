"""Leetcode #88  合并两个有序数组"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        iterations = m + n
        i, j = 0, 0
        while iterations > 0 and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                k = len(nums1) - 1
                while k > i:
                    nums1[k] = nums1[k-1]
                    k -= 1
                nums1[i] = nums2[j]
                i += 1
                j += 1
            iterations -= 1

        residual = n - j + 1
        nums1[:-residual:-1] = nums2[:-residual:-1]

    def merge2(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        双指针法
        """
        pa, pb = m - 1, n - 1
        end = m + n - 1
        while pa >= 0 or pb >= 0:
            if pa == -1:
                A[end] = B[pb]
                pb -= 1
            elif pb == -1:
                A[end] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[end] = A[pa]
                pa -= 1
            else:
                A[end] = B[pb]
                pb -= 1
            end -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)

A = [1, 2, 3, 0, 0, 0]
m = 3
B = [2, 5, 6]
n = 3

sol = Solution()
print(sol.merge2(A, m, B, n))
print(A)
