class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        if len(nums) == 0:
            return 0
        c = []
        for i in n:
            if i-1 not in n:
                y = i
                while y in n:
                    y += 1
                c.append(y-i)
        return max(c)

