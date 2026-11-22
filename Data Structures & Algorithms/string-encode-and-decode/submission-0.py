class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ''
        for i in strs:
            l = len(i)
            en = en + str(l) + '#' + i 
        return en


    def decode(self, s: str) -> List[str]:
        li = []
        i = 0
        length = len(s)
        num = ''
        temp = ''
        while i < length:
            if s[i] == '#':
                temp = temp + s[i + 1: int(num) + i + 1]
                li.append(temp)
                temp = ''
                i = i + int(num) + 1
                num = ''
                continue
            num = num + s[i]
            i = i + 1
        return li
            
                