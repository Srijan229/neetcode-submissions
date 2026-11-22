class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        maxp = 0
        for p in prices:
            if p < min:
                min = p
            else:
                maxp = max(maxp, p-min)
        return maxp