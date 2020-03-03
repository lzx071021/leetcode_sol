from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
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


A = [1, 2, 3, 0, 0, 0]
m = 3
B = [2, 5, 6]
n = 3

# A = [1]
# m = 1
# B = []
# n = 0

sol = Solution()
print(sol.merge(A, m, B, n))
print(A)
