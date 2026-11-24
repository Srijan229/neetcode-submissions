class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        low = prices[0]
        i = 1
        m = 0
        
        while i < l:
            m = max(m, prices[i] - low)
            low = min(low, prices[i])
            i += 1
        return m
            