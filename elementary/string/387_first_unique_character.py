"""Leetcode #387 字符串中的第一个唯一字符"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_cnt_idx = {}
        for idx, char in enumerate(s):
            if char not in letter_cnt_idx:
                letter_cnt_idx[char] = [1, idx]
            else:
                letter_cnt_idx[char][0] += 1

        for cnt_idx in letter_cnt_idx.values():
            if cnt_idx[0] == 1:
                return cnt_idx[1]
        return -1


test_case = {
    'leetcode': 0,
    'loveleetcode': 2
}
