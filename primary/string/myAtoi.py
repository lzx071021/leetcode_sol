import string


class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        start = 0
        for i, char in enumerate(str):
            if char != ' ':
                start = i
                break
        if str[start] in '+-' + string.digits:
            for i, char in enumerate(str[start+1:], start+1):
                if char not in string.digits:
                    str = str[start:i]
                    break
            if len(str) == 1 and str[0] in '+-':
                return 0
            else:
                num = int(str)
                return max(min(num, INT_MAX), INT_MIN)
                # if num > INT_MAX:
                #     return INT_MAX
                # elif num < INT_MIN:
                #     return INT_MIN
                # else:
                #     return num
        else:
            return 0


sol = Solution()
tst = '-42'
tst1 = '4193 with words'
tst2 = 'words and 987'
tst3 = '   -42'
tst4 = '-91283472332'
tst5 = '3.14159'
tst6 = '    -88827   5655  U'
tst7 = ''
tst8 = '     '

print(sol.myAtoi(tst1))
