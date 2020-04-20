"""Leetcode #278 第一个错误的版本"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool


def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        def binary_search(low, high):
            if low >= high:
                return low
            mid = (low+high) // 2
            if isBadVersion(mid):
                return binary_search(low, mid)
            else:
                return binary_search(mid+1, high)

        return binary_search(low, high)
