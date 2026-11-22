class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = enumerate(nums)
        for i,num in n:
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
