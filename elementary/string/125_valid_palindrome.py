"""Leetcode #125 验证回文字符串 https://leetcode-cn.com/problems/valid-palindrome/"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TODO More concise implementation
        i, j = 0, len(s) - 1
        cnt = 0
        for char in s:
            cnt += 1 if not char.isalnum() else 0
        if cnt == len(s):
            return True
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if i > j and s[i].lower() == s[j].lower():
                return True
            if i > j or s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


test_case = {
    'A man, a plan, a canal: Panama': True,
    'race a car': False
}
