from collections import defaultdict


def strStr(text, pattern):
    """KMP"""

    if not pattern:
        return 0

    def get_pmt(pattern):
        pmt = {}
        for i in range(len(pattern)):
            sub_pattern = pattern[:i+1]
            for j in range(len(sub_pattern)-1):
                if sub_pattern[:j+1] == sub_pattern[-(j+1):]:
                    if pmt.get(i, 0) < len(sub_pattern[:j+1]):
                        pmt[i] = len(sub_pattern[:j+1])
        return pmt

    pmt = get_pmt(pattern)
    i, j = 0, 0
    while i < len(text):
        # lt, rt = text[i], pattern[j]
        if text[i] == pattern[j]:
            if j == 0:
                entry = i
            j += 1
            if j == len(pattern):
                return entry
        else:
            if j != 0:
                offset = j - pmt.get(j-1, 0)
                j -= offset
                entry += offset
                i -= 1
        i += 1


text = 'BBC ABCDAB ABCDABCDABDE'
pattern = 'ABCDABD'
# pattern1 = 'abababca'
print(strStr(text, pattern))


def getNext(p, _next):
    _next[0] = -1
    i = 0
    j = -1
    while i < len(p) - 1:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            _next[i] = j
        else:
            j = _next[j]


pattern = 'ABCDABD'
_next = [0] * len(pattern)
getNext(pattern, _next)
