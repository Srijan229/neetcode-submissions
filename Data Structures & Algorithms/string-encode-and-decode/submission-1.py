class Solution:

    def encode(self, strs: List[str]) -> str:

        l = ""
        for i in strs:
            l = l + str(len(i)) + "#" + i
        return l

    def decode(self, s: str) -> List[str]:
        l = len(s)
        r = []
        i = 0
        while i < l:
            n = ""
            while s[i] != "#":
                n = n + s[i]
                i += 1
            n = int(n)
            w = ""
            j = i + 1
            while j < i + n + 1:
                w = w + s[j]
                j = j + 1
            r.append(w)
            i = j 
        return r

##
                