class Solution:
    def isHappy(self, n: int) -> bool:
        def mul(n):
            sum = 0
            while n > 0:
                a = n % 10
                sum = sum + a*a
                n = n // 10
            return sum
        check = set()
        
        while True:
            if n not in check:
                b = mul(n)
                if b == 1:
                    return True
                check.add(n)
                n = b
                
            else:
                return False
