"""Leetcode #73 矩阵置零"""
from typing import List


class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set, col_set = set(), set()
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    row_set.add(i)
                    col_set.add(j)
        for i in row_set:
            matrix[i] = [0 for _ in range(len(matrix[i]))]
        for row in matrix:
            for j in col_set:
                row[j] = 0

        # * Better implementation for setting zeros
        # for i in range(row):
        #     for j in range(col):
        #         if i in row_zero or j in col_zero:
        #             matrix[i][j] = 0


matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
expected = [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1]
]

matrix1 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
expected1 = [
    [0, 0, 0, 0],
    [0, 4, 5, 0],
    [0, 3, 1, 0]
]
print('Before:\n', matrix)
sol = Solution()
sol.setZeros(matrix)
print('After:\n', matrix)
print('Expected:\n', expected)
