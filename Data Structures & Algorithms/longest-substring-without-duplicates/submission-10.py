class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        le = len(s)
        seen = set()
        l = 0
        best = 0
        for r in range(le):
            while s[r] in seen:
                seen.remove(s[l])
                l = l + 1
            seen.add(s[r])
            best = max(best,r - l + 1)
        return best