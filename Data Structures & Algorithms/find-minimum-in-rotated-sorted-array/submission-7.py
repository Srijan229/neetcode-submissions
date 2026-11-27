class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 2
        if nums[i] <nums[-1]:
            return nums[i]
        else:
            n = nums[-1]
            while nums[j] < n:
                j -= 1
            return nums[j + 1]
