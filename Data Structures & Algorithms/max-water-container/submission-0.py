class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        arr = []
        while( i < j):
            area = (j - i) * min(heights[i], heights[j])
            arr.append(area)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return max(arr)

