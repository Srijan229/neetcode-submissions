class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        l = {}
        c = len(t)

        for ch in t:
            l[ch] = l.get(ch, 0) + 1

        i = 0
        best_start = 0
        best_len = len(s) + 1

        for j, ch in enumerate(s):
            if ch in l:
                l[ch] -= 1
                if l[ch] >= 0:
                    c -= 1

            while c == 0:
                window_len = j - i + 1
                if window_len < best_len:
                    best_start = i
                    best_len = window_len

                outgoing = s[i]
                if outgoing in l:
                    l[outgoing] += 1
                    if l[outgoing] > 0:
                        c += 1
                i += 1

        if best_len > len(s):
            return ""

        return s[best_start:best_start + best_len]