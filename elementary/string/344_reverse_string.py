"""Leetcode #344 反转字符串"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        string = ''
        for char in s:
            string = char + string
        for i in range(len(s)):
            s[i] = string[i]


test_case = {
    ["h", "e", "l", "l", "o"]: ["o", "l", "l", "e", "h"],
    ["H", "a", "n", "n", "a", "h"]: ["h", "a", "n", "n", "a", "H"]
}
