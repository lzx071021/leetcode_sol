"""Leetcode #3 无重复字符的最长子串 https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sliding = defaultdict(lambda: 0)
        i = 0
        for i, char in enumerate(s):
            if len(sliding) > max_len:
                max_len = len(sliding)
            left_border = sliding[char]
            for key in list(sliding):
                if sliding[key] < left_border:
                    sliding.pop(key)
            sliding[char] = i
        if sliding and len(sliding) > max_len:
            max_len = len(sliding)
        return max_len

    def sliding_lengthOfLongestSubstring(self, s: str) -> int:
        # TODO sliding-window version to be implemented
        pass


test_case = {
    'abcabcbb': 3,
    'bbbbb': 1,
    'pwwkew': 3,
    'dvdf': 3,
    ' ': 1
}

sol = Solution()
for case, expected in test_case.items():
    print('Result:', sol.lengthOfLongestSubstring(case))
    print('Expected:', expected)
