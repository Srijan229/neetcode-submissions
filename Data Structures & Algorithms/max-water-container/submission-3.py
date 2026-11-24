class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        i = 0
        j = l - 1
        m = 0

        while i < j:
            if heights[i] <= heights[j]:
                a = heights[i] * (j - i)
                i += 1
            elif heights[i] > heights[j]:
                a = heights[j] * (j - i)
                j -= 1
            if a > m:
                m = a
        return m
                
