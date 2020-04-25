"""Leetcode #20 有效的括号"""


class Solution:
    def isValid(self, s: str) -> bool:
        parenthsis_to_int = {
            '(': 1,
            ')': -1,
            '[': 2,
            ']': -2,
            '{': 3,
            '}': -3
        }
        sentinel = 100
        stack = [sentinel]
        for parenthsis in s:
            value = parenthsis_to_int[parenthsis]
            if value > 0:
                stack.append(value)
            elif stack and value + stack.pop() != 0:
                return False
        return True if len(stack) == 1 else False


sol = Solution()
test_case = {
    '': True,
    '(': False,
    '()': True,
    '()[]{}': True,
    '(]': False,
    '([)]': False,
    '{[]}': True,
    '}]){[(': False
}
for case, expected in test_case.items():
    print('Actual result: {}, Expected result: {}'.format(
        sol.isValid(case), expected))
