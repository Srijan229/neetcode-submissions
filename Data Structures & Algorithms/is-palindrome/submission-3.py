class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s:
            if i == " " or not i.isalnum():
                continue
            else:
                s1 = s1 + i.lower()
        if s1 == s1[::-1]:
            return True
        else:
            return False

