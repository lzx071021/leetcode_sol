from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        elif len(strs) == 1:
            return strs[0]

        strs = sorted(strs, key=len)
        first_s = strs[0]
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if s[i] != first_s[i]:
                    return first_s[:i]
        return first_s


strs = ["flower", "flow", "flight"]  # >>> fl
strs1 = ['c', 'c']                   # >>> c
strs2 = ['']                         # >>>
sol = Solution()
print(sol.longestCommonPrefix(strs))
