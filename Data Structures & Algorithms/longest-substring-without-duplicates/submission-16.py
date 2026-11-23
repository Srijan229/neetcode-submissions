class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = set()
        i,j = 0,0
        sum = 0
        while j < len(s):
            if s[j] in l:
                
                while True:
                    if s[i] == s[j]:
                        l.remove(s[i])
                        i = i + 1
                        break
                    l.remove(s[i])
                    i = i + 1
                l.add(s[j])
            else:
                l.add(s[j])
            j = j + 1
            if j - i > sum:
                sum = j - i
        return sum
                