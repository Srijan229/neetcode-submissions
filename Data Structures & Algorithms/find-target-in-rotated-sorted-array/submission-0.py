class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        for i in range(l):
            if nums[i] == target:
                return i
        return -1