"""Leetcode #66 加一"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)

        real_number = 0
        for digit in digits:
            real_number += digit * pow(10, length-1)
            length -= 1

        real_number += 1
        digits_new = []
        for i in range(len(digits)+1, 0, -1):
            diff = real_number % pow(10, i) - real_number % pow(10, i-1)
            digit = diff / pow(10, i-1)
            digits_new.append(int(digit))

        if digits_new[0] == 0:
            digits_new.remove(0)

        return digits_new


test_case = {
    [1, 2, 3]: [1, 2, 4],
    [4, 3, 2, 1]: [4, 3, 2, 2]
}
