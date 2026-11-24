class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        r = []
        i = 0

        while i < len(s):
            j = s.index("#", i)
            n = int(s[i:j])

            start = j + 1
            i = start + n
            r.append(s[start:i])

        return r