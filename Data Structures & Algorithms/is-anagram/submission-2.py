class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = []
        m = []
        for i in s:
            l.append(i)
        for i in t:
            m.append(i)
        l.sort()
        m.sort()
        if l == m:
            return True
        return False
