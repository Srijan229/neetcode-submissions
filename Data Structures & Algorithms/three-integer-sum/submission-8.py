class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = set()
        l = len(nums)
        v = set()

        for i in range(l - 2):
            if nums[i] in v:
                continue
            else:
                v.add(nums[i])
            
            if nums[i] > 0:
                break
            j = i + 1
            k = l - 1
            while j < k:
                t = nums[i] + nums[j] + nums[k]
                if t < 0:
                    j += 1
                elif t > 0:
                    k -= 1
                else:
                    r.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return list(r)
            