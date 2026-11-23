class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = {}
        for i in s:
            if i not in l:
                l[i] = 1
                continue
            l[i] += 1
        for i in t:
            if i not in l:
                return False
            l[i] -= 1
        for i in l:
            if l[i] != 0:
                return False
        return True