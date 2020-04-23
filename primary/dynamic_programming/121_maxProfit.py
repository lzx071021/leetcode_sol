"""Leetcode #121 买卖股票的最佳时机"""

from typing import List
from collections import defaultdict


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        m = defaultdict(lambda: 0)
        min_price = float('inf')
        for i in range(n):
            min_price = min(min_price, prices[i])
            m[i] = max(m[i-1], prices[i]-min_price)
        return m[n-1]


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
prices1 = [7, 6, 4, 3, 1]
print(sol.maxProfit(prices))
print(sol.maxProfit(prices1))
