"""Leetcode #190 颠倒二进制位"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # ! Cannot use while n. Because there maybe zeros in the beginning of the binary bits.
        for _ in range(32):
            res <<= 1
            res += n & 1
            n >>= 1
        return res


sol = Solution()
test_case = {
    43261596: 964176192,
    4294967293: 3221225471
}
print('Get:', list(map(sol.reverseBits, test_case.keys())))
print('Expected:', list(test_case.values()))
