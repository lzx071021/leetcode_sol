"""Leetcode #5 最长回文子串 https://leetcode-cn.com/problems/longest-palindromic-substring/"""
from typing import List


class Solution:
    # TODO
    def longestPalindrome(self, s: str) -> str:
        """Dynamic Programming"""
        n = len(s)
        max_len = 0
        longest_palindrome = ''
        for i in range(n):
            boundary = self.record_palindrome_boundary(s, i)
            palindrome = s[boundary[0]:boundary[1]+1]
            curr_len = boundary[1] - boundary[0] + 1
            if curr_len > max_len:
                max_len = curr_len
                longest_palindrome = palindrome
        return longest_palindrome

    def record_palindrome_boundary(self, s: str, i: int) -> List[int]:
        boundary = ['left_boundary', 'right_boundary']
        n = len(s)
        j = 0
        while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
            j += 1
        boundary[0], boundary[1] = i - j + 1, i + j - 1
        return boundary


test_case = {
    'babad': 'bab',
    'cbbd': 'bb'
}

sol = Solution()
for case, exp in test_case.items():
    print('Result:', sol.longestPalindrome(case))
    print('Expected:', exp)
