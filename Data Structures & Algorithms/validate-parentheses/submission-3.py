class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i in ['(','[','{']:
                l.append(i)
            if len(l) == 0:
                return False
            elif i ==')' :
                if l.pop() == '(':
                    continue
                else:
                    return False
            elif i ==']':
                if l.pop() == '[':
                    continue
                else:
                    return False
            elif i =='}':
                if l.pop() == '{':
                    continue
                else:
                    return False
        if len(l) == 0:
            return True
        else:
            return False
                