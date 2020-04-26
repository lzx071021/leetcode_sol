"""Leetcode #247 有效的字母异位词"""
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1, cnt2 = collections.Counter(s), collections.Counter(t)
        for key, value in cnt1.items():
            if cnt2[key] != value:
                return False
        return True if len(s) == len(t) else False


test_case = {
    ('anagram', 'nagaram'): True,
    ('rat', 'car'): False
}
