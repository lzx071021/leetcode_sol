class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        res = 0
        stack = []
        for char in reversed(s):
            stack.append(char)
        while stack:
            prev = stack.pop()
            curr = stack[-1] if stack else 'sentinel'
            if prev + curr in roman_to_int:
                res += roman_to_int[prev+curr]
                stack.pop()
            else:
                res += roman_to_int[prev]
        return res


sol = Solution()
# # * Expected integers: 3, 4, 58, 1994
test_case = ['III', 'IV', 'LVIII', 'MCMXCIV']
for case in test_case:
    print(sol.romanToInt(case))
