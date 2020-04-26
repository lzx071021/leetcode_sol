"""Leetcode #412 Fizz Buzz"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res

    def better_fizzBuzz(self, n: int) -> List[str]:
        checker = {
            lambda x: not x % 3: 'Fizz',
            lambda x: not x % 5: 'Buzz'
        }

        res = []
        for i in range(1, n+1):
            tmp = ''
            for key, value in checker.items():
                if key(i):
                    tmp += value
            res.append(tmp) if tmp else res.append(str(i))

        return res


sol = Solution()
# print(sol.fizzBuzz(15))
print(sol.better_fizzBuzz(15))
