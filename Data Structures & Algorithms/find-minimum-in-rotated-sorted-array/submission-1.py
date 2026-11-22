class Solution:
    def findMin(self, nums: List[int]) -> int:
        c = nums[0]
        for i in nums:
            if i < c:
                return i
        return c
