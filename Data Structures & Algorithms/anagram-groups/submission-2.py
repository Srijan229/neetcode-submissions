class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            l = list(i)
            l.sort()
            l = tuple(l)
            if l in d:
                d[l].append(i)
            else:
                d[l] = [i]
        return list(d.values())
