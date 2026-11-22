class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        
        # Loop runs as long as 'n' is a new, unseen number
        while n not in check:
            if n == 1:
                return True
            check.add(n)
            
            # One-liner to square digits: converts 19 to '1' and '9', squares them, and sums them up
            n = sum(int(digit) ** 2 for digit in str(n))
            
        return False
