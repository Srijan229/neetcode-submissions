class Solution:
    def search(self, nums: List[int], target: int) -> int:
        j = len(nums) - 1
        i = 0
        if target < nums[0]:
            if target <= nums[-1]:
                while j > 0 and nums[j] != target:
                    j -= 1
                if nums[j] == target:
                    return j
        else:
            while i < j and nums[i] != target:
                i += 1
            if nums[i] == target:
                return i
        return -1
