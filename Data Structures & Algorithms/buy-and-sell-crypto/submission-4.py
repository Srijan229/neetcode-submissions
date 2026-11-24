class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        
        j = l - 1
        m = 0
        
        while j > 0:
            i = 0
            if j != l - 1:
                if prices[j] < prices[j + 1]:
                    j -= 1
                    continue
            while i < j:
                if prices[j] - prices[i] > m:
                    m = prices[j] - prices[i]
                i += 1
            j -= 1
        return m
            