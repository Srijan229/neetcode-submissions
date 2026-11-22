class Solution:
    def isHappy(self, n: int) -> bool:
        
        check = set()

        while n != 1:
            if n in check:
                return False
            check.add(n)
            
            n = sum(int(digit) ** 2 for digit in str(n))

        return True