"""Leetcode #7 整数反转"""


class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(x)[::-1]
        if str_num.endswith('-'):
            str_num = '-' + str_num[:-1]
            return int(str_num) if int(str_num) >= -2**31 else 0
        return int(str_num) if int(str_num) <= 2**31 - 1 else 0


test_case = {
    123: 321,
    -123: -321,
    120: 21
}
