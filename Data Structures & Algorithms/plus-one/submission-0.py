class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = 0

        for digit in digits:
            n = (n * 10) + digit

        n = n + 1
        l = []

        while n > 0:
            l.append(n % 10)
            n = n // 10
        return l[::-1]

        