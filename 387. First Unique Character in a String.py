from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i in s:
            if i in c and c[i] == 1:
                return s.index(i)
        return -1
