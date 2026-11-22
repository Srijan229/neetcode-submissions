class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        d1 = {}
        for i in t:
            if i in d1:
                d1[i] = d1[i] + 1
            else:
                d1[i] = 1
        if d == d1:
            return True
        return False