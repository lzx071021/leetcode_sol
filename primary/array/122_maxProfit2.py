"""Leetcode #122 买卖股票的最佳时机 II"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Greedy"""

        max_profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                max_profit += diff
        return max_profit


test_case = {
    [7, 1, 5, 3, 6, 4]: 7,
    [1, 2, 3, 4, 5]: 4
}
