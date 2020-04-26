"""Leetcode #118 杨辉三角"""
from typing import List
from collections import defaultdict


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        raw_triangle = defaultdict(lambda: defaultdict(lambda: 0))
        raw_triangle[0][0] = 1
        for i in range(1, numRows):
            for j in range(i+1):
                raw_triangle[i][j] = raw_triangle[i-1][j] + \
                    raw_triangle[i-1][j-1]
        pascal_triangle = [[] for _ in range(numRows)]
        for row, col in raw_triangle.items():
            pascal_triangle[row] = list(
                filter(lambda x: x > 0, col.values()))
        return pascal_triangle


sol = Solution()
print(sol.generate(0))
print(sol.generate(1))
print(sol.generate(3))
print(sol.generate(5))
